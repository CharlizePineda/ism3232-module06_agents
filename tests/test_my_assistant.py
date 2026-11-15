from appointment_toolbox import AppointmentToolbox
from booking_queue import BookingQueue
from fake_model import FakeModel
from keyword_model import KeywordModel
from my_assistant import AppointmentAssistant
from my_tool import AppointmentList


class SilentModel:
    """A model that never has an answer. It stands in for Ollama being switched off."""

    def decide(self, instructions, history, tools):
        return None


def make_assistant(model):
    """Build a fresh assistant with its own tools and the model it is given."""
    appointments = AppointmentList({"monday": "9am, 10am", "tuesday": "none"})
    tools = AppointmentToolbox(appointments, BookingQueue(appointments))
    return AppointmentAssistant(
        "Karen",
        "You help patients book appointments for Greenwood Dental.",
        tools,
        model,
    )


def booking(day, time, patient):
    """Build the decision a model returns when it wants to request a booking."""
    arguments = {"day": day, "time": time, "patient": patient}
    return {"tool": "request_booking", "arguments": arguments}


def test_tool_finds_known_day():
    tool = AppointmentList({"monday": "9am, 10am"})
    assert tool.find_day("I want an appointment on Monday") == "monday"


def test_tool_returns_none_for_unknown_day():
    tool = AppointmentList({"monday": "9am, 10am"})
    assert tool.find_day("I want an appointment on Sunday") is None


def test_model_can_ask_for_open_times():
    model = FakeModel(
        [
            {"tool": "check_open_times", "arguments": {"day": "Monday"}},
            {"text": "Monday has 9am and 10am."},
        ]
    )
    assistant = make_assistant(model)
    assistant.respond("What times are open on Monday?")
    assert assistant.history[1]["content"] == "Open times on monday: 9am, 10am."


def test_booking_waits_for_the_front_desk():
    model = FakeModel([booking("monday", "9am", "Tom Smith"), {"text": "Sent."}])
    assistant = make_assistant(model)
    assistant.respond("Please book Monday at 9am for Tom Smith")
    assert len(assistant.tools.booking_queue.waiting()) == 1
    assert assistant.tools.appointment_list.bookings == []


def test_made_up_name_is_refused():
    model = FakeModel([booking("monday", "9am", "Jane Doe"), {"text": "Name?"}])
    assistant = make_assistant(model)
    assistant.respond("Please book Monday at 9am")
    assert "has not given that name" in assistant.history[1]["content"]
    assert assistant.tools.booking_queue.waiting() == []


def test_made_up_time_is_refused():
    model = FakeModel([booking("monday", "10am", "Dana Cruz"), {"text": "Time?"}])
    assistant = make_assistant(model)
    assistant.respond("Please book Monday for Dana Cruz")
    assert "has not given that time" in assistant.history[1]["content"]
    assert assistant.tools.booking_queue.waiting() == []


def test_unknown_tool_is_refused():
    model = FakeModel([{"tool": "delete_everything", "arguments": {}}, {"text": "No."}])
    assistant = make_assistant(model)
    assistant.respond("Please delete everything")
    assert "There is no tool named" in assistant.history[1]["content"]


def test_approval_records_the_booking_once():
    appointments = AppointmentList({"monday": "9am, 10am"})
    queue = BookingQueue(appointments)
    queue.request_booking("monday", "9am", "Tom Smith")
    queue.approve(1)
    queue.approve(1)
    assert len(appointments.bookings) == 1


def test_cancel_request_goes_to_front_desk():
    model = FakeModel([])
    assistant = make_assistant(model)
    assert "front desk" in assistant.respond("Please cancel my appointment")
    assert model.calls == 0


def test_silent_model_gets_a_safe_reply():
    assistant = make_assistant(SilentModel())
    assert "try again" in assistant.respond("What is the weather today?")


def test_keyword_model_still_greets():
    assistant = make_assistant(KeywordModel())
    assert assistant.respond("hello") == "Hello! How can I help you today?"


def test_history_grows_by_two_each_turn():
    assistant = make_assistant(KeywordModel())
    assistant.respond("hello")
    assistant.respond("What is open on Friday?")
    assert len(assistant.history) == 4

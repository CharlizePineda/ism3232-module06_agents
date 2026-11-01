from my_assistant import AppointmentAssistant
from my_tool import AppointmentList


def make_assistant():
    """Build a fresh assistant with its own tool for each test."""
    my_tool = AppointmentList(
        {
            "monday": "9am, 10am",
            "tuesday": "none",
        }
    )
    return AppointmentAssistant(
        "Karen", "You help clients book appointments for Greenwood Dental.", my_tool
    )


def test_tool_finds_known_day():
    tool = AppointmentList({"monday": "9am, 10am"})
    assert tool.find_day("I want an appointment on Monday") == "monday"


def test_tool_returns_none_for_unknown_day():
    tool = AppointmentList({"monday": "9am, 10am"})
    assert tool.find_day("I want an appointment on Sunday") is None


def test_cancel_request_goes_to_a_human():
    assistant = make_assistant()
    assert "human" in assistant.respond("Please cancel my appointment")


def test_unknown_request_gets_a_safe_reply():
    assistant = make_assistant()
    assert "not sure" in assistant.respond("What is the weather today?")

# my_assistant.py
# Author: Charlize Pineda


HANDSOFF_WORDS = ["reschedule", "cancel", "change", "emergency"]


class AppointmentAssistant:
    """A mock appointment assistant. Its replies come from simple rules, not from AI."""

    def __init__(self, name, instructions, my_tool):
        """Set up one assistant with its own name, instructions, tool, and history."""
        self.name = name
        self.instructions = instructions
        self.my_tool = my_tool
        self.history = []
        self.selected_day = None

    def respond(self, user_message):
        """Record the user's message, choose a reply, record it, and return it."""
        self.history.append({"role": "user", "content": user_message})
        reply = self.choose_reply(user_message)
        self.history.append({"role": "assistant", "content": reply})
        return reply

    def choose_reply(self, user_message):
        """Choose a reply with keyword rules. This is the mock part."""
        text = user_message.lower()
        appointment_words = [
            "appointment",
            "book",
            "schedule",
            "availability",
            "open",
            "time",
            "available",
        ]
        if self.needs_human(text):
            return "I can't help with that here. I'm passing you to a human agent."
        if self.selected_day is not None:
            chosen_time = self.find_time(text)
            if chosen_time:
                day = self.selected_day
                self.selected_day = None  # reset for the next booking
                return f"You're all set! Your appointment is confirmed for {day} at {chosen_time}. See you then!"
        if (
            any(word in text for word in appointment_words)
            or self.my_tool.find_day(text) is not None
        ):
            return self.appointment_reply(user_message)
        if "hello" in text:
            return (
                f"Hello! I'm {self.name}. I can help you book or manage appointments."
            )
        return "I'm not sure how to help with that. I can assist with booking appointments."

    def needs_human(self, text):
        """Return True if the message is about something a person must handle."""
        for word in HANDSOFF_WORDS:
            if word in text:
                return True
        return False

    def appointment_reply(self, user_message):
        """Check availability and confirm selected appointment time."""
        day = self.my_tool.find_day(user_message)
        if day is None:
            return "Which day? Please specify a day of the week for your appointment."
        times = self.my_tool.day_time(day)
        if times is None or times == "none":
            return f"Sorry, {day} is fully booked. Please choose another day."
        self.selected_day = day
        return f"Available times on {day}: {times}. Which time would you prefer?"

    def find_time(self, text):
        """Return the chosen time if it is available on the selected day."""
        times = self.my_tool.day_time(self.selected_day)
        cleaned = text.replace(" ", "")  # lets "9 am" match "9am"
        for t in times.split(","):
            t = t.strip()
            if t in cleaned:
                return t
        return None

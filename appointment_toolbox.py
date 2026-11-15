# appointment_toolbox.py
# Author: Charlize Pineda


class AppointmentToolbox:
    """Every tool request from the model comes and is checked here."""

    def __init__(self, appointment_list, booking_queue):
        """Hold the tools the model is allowed to ask for."""
        self.appointment_list = appointment_list
        self.booking_queue = booking_queue

    def tool_list(self):
        """Return the tools the model may ask for. They're not called here."""
        return [
            self.appointment_list.check_open_times,
            self.booking_queue.request_booking,
        ]

    def run(self, name, arguments, history):
        """Check one tool request. Run the tool only if every check passes."""
        if name == "check_open_times":
            day = self.clean(arguments, "day")
            if day == "":
                return "The day is missing. Ask the patient which day."
            return self.appointment_list.check_open_times(day)
        if name == "request_booking":
            day = self.clean(arguments, "day")
            time = self.clean(arguments, "time")
            patient = self.clean(arguments, "patient")
            if day == "" or time == "" or patient == "":
                return "The day, the time, and the patient's name are all needed."
            if not self.patient_said(history, time):
                return "The patient has not given that time. Ask them for it."
            if not self.patient_said(history, patient):
                return "The patient has not given that name. Ask them for it."
            return self.booking_queue.request_booking(day, time, patient)
        return f"There is no tool named {name}."

    def clean(self, arguments, key):
        """Return one argument as text without extra spaces, or "" if it is missing."""
        return str(arguments.get(key, "")).strip()

    def patient_said(self, history, text):
        """Return True if text appears in a message the patient typed."""
        for message in history:
            if message["role"] == "user" and text.lower() in message["content"].lower():
                return True
        return False

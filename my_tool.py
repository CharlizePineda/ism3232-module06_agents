# my_tool.py
# Author: Charlize Pineda


class AppointmentList:
    """A tool that knows the availability for appointments."""

    def __init__(self, open_times):
        """Store the available times this tool can look up"""
        self.open_times = open_times

    def find_day(self, text):
        """Return the first known day mentioned in the text, or None"""
        for day in self.open_times:
            if day in text.lower():
                return day
        return None

    def day_time(self, day):
        """Return the available times during that specific day, or None if day is fully booked."""
        if day in self.open_times:
            return self.open_times[day]
        return None

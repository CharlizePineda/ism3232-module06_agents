# my_tool.py
# Author: Charlize Pineda


class AppointmentList:
    """A tool that knows the availability for appointments."""

    def __init__(self, open_times):
        """Store the available times this tool can look up and start with no bookings."""
        self.open_times = open_times
        self.bookings = []

    def find_day(self, text):
        """Return the first known day mentioned in the text, or None"""
        for day in self.open_times:
            if day in text.lower():
                return day
        return None

    def day_time(self, day):
        """Return the available times for one day, or None if day is unknown."""
        if day in self.open_times:
            return self.open_times[day]
        return None

    def check_open_times(self, day):
        """Look up the open appointment times on one day.

        Args:
            day: The day of the week, like Monday.
        """
        found = self.find_day(day)
        if found is None:
            return "That day wasn't found. I can check Monday, Wednesday, or Friday."
        return f"Open times on {found}: {self.day_time(found)}."

    def add_booking(self, day, time, patient):
        """Record one booking. Only an approval calls this."""
        self.bookings.append({"day": day, "time": time, "patient": patient})

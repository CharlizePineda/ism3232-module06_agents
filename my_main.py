# my_main.py
# Author: Charlize Pineda

from my_assistant import AppointmentAssistant
from my_tool import AppointmentList

OPEN_TIMES = {
    "monday": "9am, 10am",
    "tuesday": "none",
    "wednesday": "9am, 12pm",
    "thursday": "none",
    "friday": "none",
    "saturday": "none",
    "sunday": "none",
}

appointment_booking = AppointmentList(OPEN_TIMES)
assistant = AppointmentAssistant(
    "Karen",
    "You help clients book appointments for Greenwood Dental.",
    appointment_booking,
)

print("type a message, or type quit to stop.")
user_message = input("You: ")
while user_message != "quit":
    print(f"{assistant.name}: {assistant.respond(user_message)}")
    user_message = input("You: ")

print(f"Messages in this conversation: {len(assistant.history)}")

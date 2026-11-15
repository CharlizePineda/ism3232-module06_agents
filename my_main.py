# my_main.py
# Author: Charlize Pineda

from appointment_toolbox import AppointmentToolbox
from booking_queue import BookingQueue
from my_assistant import AppointmentAssistant
from my_tool import AppointmentList
from ollama_model import OllamaModel

OPEN_TIMES = {
    "monday": "9am, 10am",
    "tuesday": "none",
    "wednesday": "9am, 12pm",
    "thursday": "none",
    "friday": "9am, 12pm",
    "saturday": "none",
    "sunday": "none",
}

INSTRUCTIONS = """You are Karen, a support assistant for Greenwood Dental.
Answer in one short sentence
If the patient only says hello, greet them and ask how you can help.
The office is on Main Street, across from the library.
Bring a photo ID and your insurance card to your appointment.
To make an appointment, you need the day, time, and the patient's full name.
Only state facts that appear in these instructions or in tool results.
If you do not know, say you do not know and offer to pass the patient to the front desk."""

appointment_list = AppointmentList(OPEN_TIMES)
booking_queue = BookingQueue(appointment_list)
tools = AppointmentToolbox(appointment_list, booking_queue)
model = OllamaModel("granite4.1:3b")
assistant = AppointmentAssistant("Karen", INSTRUCTIONS, tools, model)

print("type a message, or type quit to stop.")
user_message = input("You: ")
while user_message != "quit":
    print(f"{assistant.name}: {assistant.respond(user_message)}")
    user_message = input("You: ")

print(f"Messages in this conversation: {len(assistant.history)}")

print("Front desk review")
for request in booking_queue.waiting():
    number = request["number"]
    print(f"Request {number}: {request['patient']}, {request['day']} {request['time']}")
    answer = input("Approve? yes or no: ")
    if answer == "yes":
        print(booking_queue.approve(number))
    else:
        print(booking_queue.reject(number))

print(f"Appointments: {len(appointment_list.bookings)}")

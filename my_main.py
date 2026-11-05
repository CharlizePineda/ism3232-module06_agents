# my_main.py
# Author: Charlize Pineda

from my_assistant import AppointmentAssistant
from my_tool import AppointmentList
from ollama_model import OllamaModel

OPEN_TIMES = {
    "monday": "9am, 10am",
    "tuesday": "none",
    "wednesday": "9am, 12pm",
    "thursday": "none",
    "friday": "none",
    "saturday": "none",
    "sunday": "none",
}

INSTRUCTIONS = """You are Karen, a support assistant for Greenwood Dental.
Answer in one short sentence
The office is on Main Street, across from the library.
Bring a photo ID and your insurance card to your appointment.
Only state facts that appear in these instructions.
If you do not know, say you do not know and offer to pass the customer to the front desk."""

appointment_booking = AppointmentList(OPEN_TIMES)
model = OllamaModel("granite4.1:3b")
assistant = AppointmentAssistant("Karen", INSTRUCTIONS, appointment_booking, model)

print("type a message, or type quit to stop.")
user_message = input("You: ")
while user_message != "quit":
    print(f"{assistant.name}: {assistant.respond(user_message)}")
    user_message = input("You: ")

print(f"Messages in this conversation: {len(assistant.history)}")

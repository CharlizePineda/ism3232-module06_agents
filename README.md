# ISM3232 Small business assistant

**Name:** Charlize Pineda
**Date:** November 1, 2026

## The Greenwood Dental assistant

This assistant helps clients book appointments with Greenwood Dental by asking for a day, listing the open times for that day, and confirming the appointment once the time is selected. The mock returns a reply based on the simple rules created and the keywords the user inputs; this doesn't use AI. Requests that go to a person are included in the HANDSOFF_WORDS, like cancel or reschedule, because there are potential charges for cancellations and rescheduling that this assistant cannot help with. If this used real customer data, the clients sensitive information stored in the history could risk exposure if there isn't any proper security measures.

The model answered the question about the location of Greenwood Dental well as it came directly from the instructions. It got one wrong when I replied "9" to choose a time and then it confirmed my appointment for 9am. The message didn't match a rule and went to the model to confirm the appointment. I kept all of my handsoffs (reschedule, cancel, change, emergency) in code because I didn't want the model to be confidently wrong in handling any of those.

The model did well answering the question about the open times for Monday and redirecting the "do you do business taxes?" question to the front desk for a human reply instead of making up an answer. Booking an appointment had more trouble. When I typed "9" and then "9am", the model kept asking me to confirm the time and the request finally only went through when I typed "9:00am" after being prompted to type it in that format. I think the toolbox refused the earlier attempts because the passing times that the model passes didn't match what I typed. I decided to keep all but one word in the handsoffs (I removed "change" and kept "cancel","reschedule", and "emergency") because this model can't be trusted to handle those requests on its own.
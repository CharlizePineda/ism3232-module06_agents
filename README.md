# ISM3232 Small business assistant

**Name:** Charlize Pineda
**Date:** November 1, 2026

## The Greenwood Dental assistant

This assistant helps clients book appointments with Greenwood Dental by asking for a day, listing the open times for that day, and confirming the appointment once the time is selected. The mock returns a reply based on the simple rules created and the keywords the user inputs; this doesn't use AI. Requests that go to a person are included in the HANDSOFF_WORDS, like cancel or reschedule, because there are potential charges for cancellations and rescheduling that this assistant cannot help with. If this used real customer data, the clients sensitive information stored in the history could risk exposure if there isn't any proper security measures.

The model answered the question about the location of Greenwood Dental well as it came directly from the instructions. It got one wrong when I replied "9" to choose a time and then it confirmed my appointment for 9am. The message didn't match a rule and went to the model to confirm the appointment. I kept all of my handsoffs (reschedule, cancel, change, emergency) in code because I didn't want the model to be confidently wrong in handling any of those.
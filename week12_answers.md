# Week 12 answers

## Exercise 1
1. The messages the customer typed: "I want to change my shipping address", "It's order A102", "9 Pine Street, Tampa"
2. How many tool requests were refused, and why: The orderid: A100 and the address of 123 Main St, Anytown, AN 12345 were refused because the user didn't type in the orderid or the address.
3. If the customer now types "thanks", how many messages does Ollama receive on the next call? Ollama receives 14, there's 6 between the user and assisstant, another 6 for the tool, one for the system and the new one would make the total 14.
4. Why does "Do you sell gift cards?" still go to a person, and why is that acceptable? Because the word "card" is in the handoff words, asking about a gift card follows the rule to take the user to a real person. This is acceptable because any type of card can contain sensitive information so sending it off to a human who has the correct knowledge is safer.

## Exercise 3
Type a message, or type quit to stop.
You: I want to change my shipping address
Sunny: Your request to change the shipping address has been submitted and is awaiting staff approval.
You: quit
Messages in this conversation: 3
Staff review
Request 1: A100 to 123 Main St, Anytown, AN 12345
Approve? yes or no: no
Request 1 rejected.
A100 14 Bay Road
A101 3 Gull Lane
A102 88 Pier Street

[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-7f7980b617ed060a017424585567c406b6ee15c891e84e1186181d67ecf80aa0.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=11407610)
ASSIGNMENT EVENT MANAGEMENT
===========================
Team Members:
--------------
1. Name:RUTAGENGWA Justin        RegNo: 221016176         Department:INFORMATION TECHINOLOGY
2. Name:GASASIRA JEAN FELIX      RegNo: 221009548         Department:INFORMATION TECHNOLOGY
3. Name:Mugeni yvonne        RegNo: 221008236         Department: COMPUTER SCIENCE
4. Name:  INGABIRE Gentille      RegNo:  221009513        Department: Computer Science 


Instructions
============
This work will have two main sections (1. practical assignment, 2. Presentation assignment)
1. Form teams of 4. Teams should be diverse (having members from both departments [IT & CS])
2. Each members participation/contribution to the work should be clear and visible through commits made.
3. Assignment grades will be individual based on contributions


Assignment Scenario
===================

You have been tasked with designing a database schema for an event management application, this application will be used to manage various events and their associated data. Based on the given requirements, create the necessary Django models to implement the following features:

Event Management:

Each event should have a title, description, start date, end date, location, category and an indication of whether it is free or requires payment. Categories should be dynamic allowing the options to manipulate them.

Speaker Management:
Each speaker should have a name, biography, optional photo, email address,phone number, and social media links (linkedin, and twitter).

Participant Management:
Each participant should have a name, email address, phone number, and the ability to attend multiple events.
Participants can attend multiple events(that are not happening at the same time).

Schedule Management:
Each event should have a schedule consisting of start and end times, a topic, and an optional speaker.

Event Payment Processing:
For paid events, implement a payment system that stores payment details.
Payment details should include the participant, event, amount paid, payment method, payment date, transaction ID, and payment status (choices: 'PAID', 'PENDING', 'FAILED').

TASKS:
------

**Task 1:**
Design the Django models to represent the above requirements. Write the necessary code in Python using the Django framework to create the models. Make sure to include all required fields, relationships, and any additional methods or attributes needed.

**TASK 2:**
Populate the models created with some dummy data reflecting a real-world scenario. create at least 100 records for each model.
Try also to diversify the data. Make sure to include your database (in json format) in the project structure.

**Task 3:**
The following covers a range of functionalities that would be required. You are tasked to write django queries corresponding to the below needs. Every query should have it own view and url endpoint. 

- a list of all events.
- details of a specific event by its title.
- list of all speakers.
- details of a specific speaker by their name.
- a list of all participants.
- details of a specific participant by their email address.
- a list of all schedules.
- schedules of a specific event.
- a list of all payments.
- payments made by a specific participant.
- the upcoming events based on the current date.
- a list of free events.
- a list of paid events.
- the count of participants for each event.
- the count of events attended by each participant.
- the count of schedules for each event.
- the total amount paid for a specific event.
- the average price of paid events.
- the list of participants attending a specific event.
- the list of speakers for a specific event.
- the events scheduled for a specific date range.
- participants who have attended all events.
- events that have no assigned speakers.
- events with the highest amount paid.
- participants who have paid the most.
- speakers who have the most scheduled events.
- events with the longest duration.
- participants who have attended the most events in a specific month.
- events with overlapping schedules.
- participants who have made a payment in the last 7 days.
- participants who have attended consecutive events.
- speakers who have not been assigned to any events.
- events with the highest total payment amount.
- participants who have attended events in multiple locations.
- speakers who have presented on different topics.
- events with the longest gap between start and end dates.
- participants who have attended events organized by a specific location.
- speakers who have the highest average rating.
- participants who have made payments for all events.

**Task 4 (Optional):**
If you want you can style (using bootstrap) each template file according to the data you will be rendering.

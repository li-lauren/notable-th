## Notable Health
### Take-Home Coding Assignment

Here I used flask as my backend framework.  I also used a PostGreSQL database
where I have separate tables for Doctors, Patients, and Appointments.  So far, 
the database is seeded with some sample data via methods in the seed.py file.

Out of the (many) things I'd like to improve, here are a few pressing ones:
- store date and time as a Python datetime object, rather than with strings 
(right now date has to be given in "MM-DD-YR" format, 
and time in "HH:MMAM"/"HH:MMPM" format)
- have more informative return statements when there is an error
- write unit tests (so far I only did some very basic testing with Postman) and 
overall do a lot more testing

Thanks for your time!
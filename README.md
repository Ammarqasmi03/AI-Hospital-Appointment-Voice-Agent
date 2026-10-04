AI-BASED HOSPITAL APPOINTMENT SYSTEM

PROJECT README / COMPLETE SETUP GUIDE

Developer: Ammar Gour Degree: MCA, Jamia Millia Islamia

1. PROJECT OVERVIEW

The AI-Based Hospital Appointment System is an AI-powered hospital
appointment management application.

The system allows patients to: - Book a new hospital appointment - View
appointments - Check appointment availability - Reschedule
appointments - Cancel appointments - View appointment history - Use an
AI Voice Assistant

Technologies: Python, FastAPI, PostgreSQL, SQLAlchemy, Pydantic,
Streamlit, Vapi AI, Twilio, Requests, Pandas, Uvicorn and Render.

2. SYSTEM ARCHITECTURE

WEB APPLICATION:

Patient | v Streamlit Frontend | | REST API v FastAPI Backend | v
SQLAlchemy | v PostgreSQL | v Appointment Records

AI VOICE APPLICATION:

Patient Phone | v Twilio | v Vapi AI Voice Assistant | v FastAPI Backend
| v SQLAlchemy | v PostgreSQL

3. PROJECT FEATURES

1.  Book Appointment
    -   Patient name
    -   Reason for visit
    -   Appointment date
    -   Appointment time

2.  My Appointments
    -   Select a date
    -   Load appointments for that date
    -   This section is mainly for checking/viewing appointments.
    -   The actual database insertion is performed by the Book
        Appointment API.

3.  Reschedule Appointment
    -   Change the date/time of an existing appointment.

4.  Cancel Appointment
    -   Cancel an existing appointment.
    -   The record remains in the database with cancelled=true.

5.  Check Availability
    -   Check available appointment slots.

6.  AI Voice Assistant
    -   Uses Vapi AI and Twilio.
    -   Supports appointment-related voice interaction.

7.  Appointment History
    -   Displays all appointment records stored in PostgreSQL.

8.  PROJECT STRUCTURE

AI-Hospital-Appointment-Voice-Agent/ | |– backend.py |– database.py |–
app_frontend.py |– requirements.txt |– README.md |– .gitignore |– .env |
|– assets/ | |– hospital-bg.jpg | |– .venv/

5. IMPORTANT FILES

backend.py Contains the FastAPI application, API endpoints, appointment
operations, validation and Vapi API integration.

database.py Contains the PostgreSQL connection, SQLAlchemy engine,
database session, Appointment model and database initialization.

app_frontend.py Contains the Streamlit interface, dashboard, appointment
forms, history and API communication.

6. DATABASE STRUCTURE

Database: hospital_appointments

Table: appointments

Columns: - Appointment_id : Integer, primary key - patient_name :
Patient name - reason : Reason for visit - start_time : Appointment date
and time - cancelled : Boolean cancellation status - created_at :
Appointment creation time

7. LOCAL POSTGRESQL SETUP

STEP 1: Install PostgreSQL.

STEP 2: Open pgAdmin.

STEP 3: Create the database:

CREATE DATABASE hospital_appointments;

STEP 4: Make sure PostgreSQL is running.

Typical local connection: Host: localhost Port: 5432

8. PYTHON ENVIRONMENT SETUP

Project folder example:

D:_Voice_Agent

STEP 1: Open PowerShell in the project folder.

STEP 2: Create a virtual environment:

python -m venv .venv

STEP 3: If PowerShell blocks activation:

Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned

STEP 4: Activate:

..venv.ps1

STEP 5: Upgrade pip:

python -m ensurepip –upgrade python -m pip install –upgrade pip

9. INSTALL DEPENDENCIES

Install requirements:

python -m pip install -r requirements.txt

If needed, install PostgreSQL driver:

python -m pip install psycopg2-binary

Install dotenv:

python -m pip install python-dotenv

10. DATABASE_URL CONFIGURATION

The PostgreSQL connection should be read from the environment.

In database.py:

import os

DATABASE_URL = os.getenv(“DATABASE_URL”)

if not DATABASE_URL: raise ValueError(“DATABASE_URL is not configured”)

Then:

engine = create_engine(DATABASE_URL)

Do not hard-code production credentials in source code.

11. LOCAL .ENV CONFIGURATION

Create:

.env

Example:

DATABASE_URL=postgresql+psycopg2://USERNAME:PASSWORD@localhost:5432/hospital_appointments
VAPI_API_KEY=YOUR_VAPI_PRIVATE_KEY

IMPORTANT: Never upload .env to GitHub.

If a PostgreSQL password contains special characters such as @, URL
encoding may be required. For example:

@ -> %40

12. .GITIGNORE

Add:

.env .venv/ pycache/ *.pyc

Never commit: - Database passwords - DATABASE_URL containing
credentials - Vapi API key - Twilio credentials

13. START FASTAPI

Run:

python -m uvicorn backend:app –reload

Backend:

http://127.0.0.1:8000

Swagger:

http://127.0.0.1:8000/docs

14. START STREAMLIT

Open another terminal.

Activate the environment:

..venv.ps1

Run:

python -m streamlit run app_frontend.py

15. FRONTEND BACKEND CONNECTION

For local development:

base_url = “http://127.0.0.1:8000”

For Render:

base_url = “https://your-render-service.onrender.com”

The Streamlit frontend communicates with FastAPI using REST API
requests.

16. BOOK APPOINTMENT WORKFLOW

The Book Appointment form collects:

Patient Name Reason for Visit Appointment Date Appointment Time

Example request:

{ “patient_name”: “Test Patient”, “reason”: “General Checkup”,
“start_time”: “2026-10-15T10:00:00” }

The request is sent to:

POST /book_appointments/

Flow:

Patient | v Book Appointment Form | v Streamlit | v POST
/book_appointments/ | v FastAPI | v SQLAlchemy | v PostgreSQL | v
Appointment Saved

17. HOW TO CHECK WHETHER THE APPOINTMENT IS SAVED

After booking an appointment, open pgAdmin.

Open:

Databases -> hospital_appointments -> Schemas -> public -> Tables ->
appointments

Open Query Tool and run:

SELECT * FROM public.appointments ORDER BY “Appointment_id” DESC;

The newest appointment should appear at the top.

Check total records:

SELECT COUNT(*) FROM public.appointments;

Check which database pgAdmin is using:

SELECT current_database();

18. VERY IMPORTANT: LOCAL POSTGRESQL VS RENDER POSTGRESQL

There can be two different databases:

1.  Local PostgreSQL
2.  Production PostgreSQL used by Render

If the local application uses:

DATABASE_URL=postgresql+psycopg2://…@localhost:5432/hospital_appointments

the appointment is saved in the local PostgreSQL database.

If Render uses another DATABASE_URL, Render saves the appointment in the
database specified by Render.

Therefore, an appointment created through Render does NOT automatically
appear in local pgAdmin unless Render is connected to that same
database.

If Render and local pgAdmin use different databases, their data will be
different.

19. MY APPOINTMENTS SECTION

The My Appointments section is used to check appointments for a selected
date.

It sends:

POST /list_appointments/

Example:

{ “date”: “2026-10-15” }

The backend returns appointments for that date.

This section is for viewing/checking records. It does not perform the
database insertion.

The database insertion is performed by:

POST /book_appointments/

20. APPOINTMENT HISTORY

The Appointment History section uses:

GET /appointment_history/

It retrieves appointment records from PostgreSQL.

The backend orders appointments by start_time.

This section can be used to confirm that newly booked appointments have
reached the database.

21. API ENDPOINTS

POST /book_appointments/ Creates a new appointment.

POST /reschedule_appointments/ Reschedules an appointment.

POST /cancel_appointments/ Cancels an appointment.

POST /check_availability/ Checks appointment availability.

POST /list_appointments/ Lists appointments for a selected date.

GET /appointment_history/ Returns appointment history.

POST /call_shifa/ Initiates the AI voice call.

22. TEST USING SWAGGER

Open:

http://127.0.0.1:8000/docs

Find:

POST /book_appointments/

Click:

Try it out

Example JSON:

{ “patient_name”: “Test Patient”, “reason”: “General Checkup”,
“start_time”: “2026-10-15T10:00:00” }

Click Execute.

If successful, check pgAdmin:

SELECT * FROM public.appointments ORDER BY “Appointment_id” DESC;

If the new record appears, the complete booking-to-database flow is
working.

23. RENDER DEPLOYMENT

STEP 1: Push the project to GitHub.

git add . git commit -m “Update hospital appointment system” git push
origin main

STEP 2: Open Render.

Select:

New -> Web Service

STEP 3: Connect the GitHub repository.

STEP 4: Build command:

pip install -r requirements.txt

STEP 5: Start command:

uvicorn backend:app –host 0.0.0.0 –port $PORT

24. RENDER ENVIRONMENT VARIABLES

Open:

Render -> Your FastAPI Service -> Environment

Add:

DATABASE_URL VAPI_API_KEY

DATABASE_URL must point to the PostgreSQL database that the Render
backend should use.

Do not use localhost for a production database unless the database is
actually running in the same environment.

Keep all credentials secret.

25. VAPI AI AND TWILIO

The voice assistant uses:

Vapi AI Twilio FastAPI

The backend reads:

VAPI_API_KEY = os.getenv(“VAPI_API_KEY”)

The Vapi configuration contains: - Assistant ID - Phone Number ID -
Customer phone number

The customer number is the patient’s phone number.

The configured Vapi phone number is the hospital/AI calling number.

26. COMMON PROBLEMS

PROBLEM: DATABASE_URL is not configured.

SOLUTION: Check .env locally or Render Environment Variables.

PROBLEM: PostgreSQL connection error.

CHECK: - PostgreSQL is running - Database name - Username - Password -
Host - Port - DATABASE_URL - psycopg2-binary

PROBLEM: pgAdmin shows zero rows after booking.

CHECK: 1. Is the application local or on Render? 2. Which DATABASE_URL
is being used? 3. Is pgAdmin connected to the same database? 4. Run:

SELECT current_database();

5.  Run:

SELECT * FROM public.appointments ORDER BY “Appointment_id” DESC;

If Render contains the appointment but local pgAdmin does not, they are
using different databases.

PROBLEM: VAPI_API_KEY is not configured.

SOLUTION: Add VAPI_API_KEY to the local .env or Render Environment
Variables.

PROBLEM: FastAPI does not start.

Try:

python -m uvicorn backend:app –reload

PROBLEM: Streamlit command does not work directly.

Try:

python -m streamlit run app_frontend.py

27. OLD SQLITE DATA MIGRATION

If the project previously used SQLite, the old database data should be
migrated carefully.

Example old database:

appointments_db.db

Do not delete the SQLite database before migration.

Migration should:

1.  Read old SQLite records.
2.  Connect to PostgreSQL.
3.  Compare existing records.
4.  Insert missing records.
5.  Verify migrated records.
6.  Verify the PostgreSQL ID sequence.

Fields to migrate:

Appointment_id patient_name reason start_time cancelled created_at

After migration:

SELECT * FROM public.appointments ORDER BY “Appointment_id” ASC;

Keep the old SQLite database as a backup until migration is verified.

28. DATABASE VERIFICATION CHECKLIST

[ ] PostgreSQL is running [ ] hospital_appointments database exists [ ]
appointments table exists [ ] DATABASE_URL is correct [ ]
psycopg2-binary is installed [ ] FastAPI starts [ ] Swagger opens [ ]
Book Appointment API works [ ] New appointment appears in PostgreSQL [ ]
My Appointments displays the appointment [ ] Appointment History
displays the appointment [ ] Reschedule works [ ] Cancel works [ ] Vapi
API key is configured [ ] Voice assistant works [ ] Render environment
variables are configured

29. COMPLETE LOCAL WORKFLOW

STEP 1: Start PostgreSQL.

STEP 2: Open the project folder.

STEP 3: Activate virtual environment:

..venv.ps1

STEP 4: Start FastAPI:

python -m uvicorn backend:app –reload

STEP 5: Open Swagger:

http://127.0.0.1:8000/docs

STEP 6: Open another terminal.

STEP 7: Activate virtual environment.

STEP 8: Run Streamlit:

python -m streamlit run app_frontend.py

STEP 9: Open Book Appointment.

STEP 10: Enter patient details.

STEP 11: Click Confirm Appointment.

STEP 12: Open pgAdmin.

STEP 13: Run:

SELECT * FROM public.appointments ORDER BY “Appointment_id” DESC;

STEP 14: Confirm the new appointment exists.

STEP 15: Open Appointment History.

STEP 16: Confirm the same appointment appears.

30. COMPLETE RENDER WORKFLOW

STEP 1: Push the latest code to GitHub.

STEP 2: Deploy FastAPI on Render.

STEP 3: Set the start command:

uvicorn backend:app –host 0.0.0.0 –port $PORT

STEP 4: Add Render environment variables:

DATABASE_URL VAPI_API_KEY

STEP 5: Redeploy.

STEP 6: Open:

https://your-render-service.onrender.com/docs

STEP 7: Test POST /book_appointments/.

STEP 8: Test GET /appointment_history/.

STEP 9: Confirm that the new appointment is returned.

STEP 10: Use the Streamlit frontend with the Render backend URL.

STEP 11: Book an appointment through the deployed application.

STEP 12: Check the SAME PostgreSQL database configured in Render.

31. SECURITY

For a real production hospital application, implement:

-   User authentication
-   Password hashing
-   Role-based access
-   HTTPS
-   API authentication
-   Input validation
-   Secure secret management
-   Database access restrictions
-   Audit logging
-   Patient data protection
-   Appropriate healthcare data compliance

32. FUTURE IMPROVEMENTS

-   Patient login
-   Doctor login
-   Admin dashboard
-   Doctor availability
-   Department management
-   Email notifications
-   SMS notifications
-   Appointment reminders
-   Calendar integration
-   Advanced AI chatbot
-   Improved voice conversation
-   Analytics dashboard
-   Role-based authorization
-   Secure authentication
-   Online payment integration

33. PROJECT OBJECTIVE

The main objective is to develop an AI-powered hospital appointment
management system that makes appointment booking and management easier
for patients.

The project combines:

Artificial Intelligence + Voice Interaction + Web Application + REST
APIs + PostgreSQL Database

34. DEVELOPER

Ammar MCA Jamia Millia Islamia

Interests: - Artificial Intelligence - Machine Learning - Data
Analytics - Python Development - Generative AI - Software Engineering

35. LICENSE

This project is developed for educational, academic and portfolio
purposes.

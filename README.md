## AI Hospital Appointment Voice Agent

An AI-powered hospital appointment booking system using Vapi AI.

## Features

- Book Appointment
- Check Availability
- Reschedule Appointment
- Cancel Appointment
- Appointment History
- Voice-based Interaction

## Architecture

User Voice
    ↓
Vapi AI Agent
    ↓
FastAPI Backend
    ↓
SQLite Database
    ↓
Streamlit Dashboard

## Tech Stack

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Streamlit
- Vapi AI
- Ngrok

## Run Locally

```bash
pip install -r requirements.txt
uv run backend.py
streamlit run app_frontend.py
pip install -r requirements.txt
uv run backend.py
streamlit run app_frontend.py

# Step1: Import database objects

import datetime as dt
from sqlalchemy import func
from sqlalchemy.orm import Session

from pydantic import BaseModel
from database import get_db, init_db, Appointment

init_db()  # Initialize the database and create tables if they don't exist

# Step3: Create data contracts using Pydantic models

class AppointmentRequest(BaseModel):
    patient_name: str
    reason: str
    start_time: dt.datetime

class AppointmentResponse(BaseModel):
    Appointment_id: int
    patient_name: str
    reason: str | None
    start_time: dt.datetime
    cancelled: bool
    created_at: dt.datetime

class RescheduleAppointmentRequest(BaseModel):
    appointment_id: int
    start_time: dt.datetime


class RescheduleAppointmentResponse(BaseModel):
    Appointment_id: int
    patient_name: str
    reason: str | None
    start_time: dt.datetime
    cancelled: bool
    created_at: dt.datetime

class cancelAppointmentRequest(BaseModel):
    appointment_id: int
    patient_name: str

class cancelAppointmentResponse(BaseModel):
   cancelled_count : int


class checkAvailabilityRequest(BaseModel):
    date: dt.date
    start_time: dt.time

class checkAvailabilityResponse(BaseModel):
    available: bool

class ListAppointmentsRequest(BaseModel):
    date : dt.date

class CallRequest(BaseModel):
    phone_number: str

# Step2: Create FastAPI app and endpoints pseudo code

from fastapi import FastAPI, Depends, HTTPException

app = FastAPI()

#Book_Appointment
@app.post("/book_appointments/")
def book_appointment(request: AppointmentRequest, db: Session = Depends(get_db)):
    new_appointment = Appointment(
        patient_name=request.patient_name,
        reason=request.reason,
        start_time=request.start_time
    )
    db.add(new_appointment)
    db.commit()
    db.refresh(new_appointment)
    new_appointment_return_obj = AppointmentResponse(
        Appointment_id=new_appointment.Appointment_id,
        patient_name=new_appointment.patient_name,
        reason=new_appointment.reason,
        start_time=new_appointment.start_time,
        cancelled=new_appointment.cancelled,
        created_at=new_appointment.created_at
    )
    return new_appointment_return_obj

    # Code to save the appointment to the database
    # write row to db



#reschedule_appointment
@app.post("/reschedule_appointments/")
def reschedule_appointment(request: RescheduleAppointmentRequest, db: Session = Depends(get_db)):
    # Code to update the appointment in the database
    # update row in db
    appointment = db.query(Appointment).filter(
        Appointment.Appointment_id == request.appointment_id
    ).first()

    if appointment is None:
        raise HTTPException(
            status_code=404,
            detail="Appointment not found"
        )

    appointment.start_time = request.start_time

    db.commit()
    db.refresh(appointment)

    return RescheduleAppointmentResponse(
        Appointment_id=appointment.Appointment_id,
        patient_name=appointment.patient_name,
        reason=appointment.reason,
        start_time=appointment.start_time,
        cancelled=appointment.cancelled,
        created_at=appointment.created_at
    )
#cancel_appointment
@app.post("/cancel_appointments/")
def cancel_appointment(request: cancelAppointmentRequest, db: Session = Depends(get_db)):
    # Code to mark the appointment as cancelled in the database
    # update row in db to set cancelled=True    
    
    appointment = db.query(Appointment).filter(
        Appointment.Appointment_id == request.appointment_id,
        Appointment.patient_name == request.patient_name
    ).first()

    if appointment is None:
        raise HTTPException(
            status_code=404,
            detail="Appointment not found"
        )

    appointment.cancelled = True

    db.commit()
    db.refresh(appointment)

    return cancelAppointmentResponse(
        cancelled_count=1
    )    

#check_appointment_Availability
@app.post("/check_availability/")
def check_availability(request: checkAvailabilityRequest, db: Session = Depends(get_db)):
    # Code to check if the appointment slot is available in the database
    # read rows from db

    request_datetime = dt.datetime.combine(request.date, request.start_time)
    
    appointment = db.query(Appointment).filter(
        Appointment.start_time == request_datetime,
        Appointment.cancelled == False
    ).first()

    available = appointment is None

    return checkAvailabilityResponse(
        available=available
    )

from datetime import datetime, time, timedelta

#List_Appointments
@app.post("/list_appointments/")
def list_appointments(request : ListAppointmentsRequest, db: Session = Depends(get_db)):
 
    start_day = datetime.combine(request.date, time.min)
    end_day = start_day + timedelta(days=1)

    appointments = (
        db.query(Appointment)
        .filter(
            Appointment.start_time >= start_day,
            Appointment.start_time < end_day
        )
        .order_by(Appointment.start_time.asc())
        .all()
    )


    appointment_list = [
        AppointmentResponse(
            Appointment_id=appt.Appointment_id,
            patient_name=appt.patient_name,
            reason=appt.reason,
            start_time=appt.start_time,
            cancelled=appt.cancelled,
            created_at=appt.created_at
        )
        for appt in appointments
    ]

    return {
        "appointments": appointment_list
    }


@app.get("/appointment_history/")
def appointment_history(db: Session = Depends(get_db)):

    appointments = (
        db.query(Appointment)
        .order_by(
            Appointment.start_time.desc()
        )
        .all()
    )

    return appointments


import os
import requests

VAPI_API_KEY = os.getenv("799aadec-0f84-4b4a-9a0a-7cb86bd01657")
    
@app.post("/call_shifa/")
def call_shifa(request: CallRequest):

    headers = {
        "Authorization": f"Bearer {VAPI_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "assistantId": "aa9c10da-7172-4846-92e9-f09e234ccff6",
        "phoneNumberId": "69129286-91ce-47de-8410-25bcfcd3e0a7",
        "customer": {
            "number": request.phone_number
        }
    }

    response = requests.post(
        "https://api.vapi.ai/call",
        headers=headers,
        json=payload
    )

    if response.status_code != 200:
        return {
            "error": response.text,
            "status": response.status_code
        }

    return response.json()





import uvicorn
if __name__ == "__main__":
    uvicorn.run("backend:app", host="127.0.0.1", port=8000, reload=True)

# Step4: Write actual code for endpoints to interact with the database
# Step5: Streamlit dashboard (just for testing)


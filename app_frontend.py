import streamlit as st
import datetime as dt
import requests

st.set_page_config(
    page_title="Hospital Appointment System",
    page_icon="🏥",
    layout="wide"
)

st.title("🏥 Hospital Appointment System")

base_url = st.text_input("Backend URL", "https://ai-hospital-appointment-voice-agent.onrender.com").rstrip("/")

# patient_name = st.text_input("Patient Name")
# reason = st.text_input("Reason for Appointment")
# start_time = st.time_input("Time", value=dt.time(9,0))
# start_date = st.date_input("Date", value=dt.date.today() + dt.timedelta(days=1))



tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(
    [
        "Book Appointment",
        "Check Availability",
        "Reschedule",
        "Cancel",
        "List Appointments",
        "History",
        "Shifa Assistant"
    ]
)

# ==========================
# BOOK APPOINTMENT
# ==========================

with tab1:

    st.header("Book Appointment")

    patient_name = st.text_input("Patient Name")

    reason = st.text_input("Reason")

    appointment_date = st.date_input(
        "Appointment Date",
        value=dt.date.today()
    )

    appointment_time = st.time_input(
        "Appointment Time",
        value=dt.time(9, 0)
    )

    if st.button("Book Appointment"):

        start_datetime = dt.datetime.combine(
            appointment_date,
            appointment_time
        )

        payload = {
            "patient_name": patient_name,
            "reason": reason,
            "start_time": start_datetime.isoformat()
        }

        response = requests.post(
            f"{base_url}/book_appointments/",
            json=payload
        )

        if response.status_code == 200:
            st.success("Appointment booked successfully")
            st.json(response.json())
        else:
            st.error(response.text)

# ==========================
# CHECK AVAILABILITY
# ==========================

with tab2:

    st.header("Check Availability")

    check_date = st.date_input(
        "Date",
        value=dt.date.today(),
        key="check_date"
    )

    check_time = st.time_input(
        "Time",
        value=dt.time(9, 0),
        key="check_time"
    )

    if st.button("Check Availability"):

        payload = {
            "date": str(check_date),
            "start_time": str(check_time)
        }

        response = requests.post(
            f"{base_url}/check_availability/",
            json=payload
        )

        if response.status_code == 200:

            available = response.json()["available"]

            if available:
                st.success("Slot Available")
            else:
                st.warning("Slot Not Available")

        else:
            st.error(response.text)

# ==========================
# RESCHEDULE
# ==========================

with tab3:

    st.header("Reschedule Appointment")

    appointment_id = st.number_input(
        "Appointment ID",
        min_value=1,
        step=1
    )

    new_date = st.date_input(
        "New Date",
        key="new_date"
    )

    new_time = st.time_input(
        "New Time",
        key="new_time"
    )

    if st.button("Reschedule"):

        payload = {
            "appointment_id": int(appointment_id),
            "start_time": dt.datetime.combine(
                new_date,
                new_time
            ).isoformat()
        }

        response = requests.post(
            f"{base_url}/reschedule_appointments/",
            json=payload
        )

        if response.status_code == 200:
            st.success("Appointment Rescheduled")
            st.json(response.json())
        else:
            st.error(response.text)

# ==========================
# CANCEL
# ==========================

with tab4:

    st.header("Cancel Appointment")

    cancel_id = st.number_input(
        "Appointment ID",
        min_value=1,
        step=1,
        key="cancel_id"
    )

    cancel_name = st.text_input(
        "Patient Name",
        key="cancel_name"
    )


    if st.button("Cancel Appointment"):

        payload = {
            "appointment_id": int(cancel_id),
            "patient_name": cancel_name,
        }

        response = requests.post(
            f"{base_url}/cancel_appointments/",
            json=payload
        )

        if response.status_code == 200:
            st.success("Appointment Cancelled")
            st.json(response.json())
        else:
            st.error(response.text)

# ==========================
# LIST APPOINTMENTS
# ==========================

with tab5:

    st.header("List Appointments")

    search_date = st.date_input(
        "Date",
        value=dt.date.today()
    )

    if st.button("Load Appointments"):

        payload = {
            "date": str(search_date)
        }

        response = requests.post(
            f"{base_url}/list_appointments/",
            json=payload
        )

        if response.status_code == 200:

            appointments = response.json()["appointments"]

            if len(appointments) == 0:
                st.info("No appointments found")
            else:
                st.dataframe(appointments)

        else:
            st.error(response.text)


with tab6:

    st.header("Appointment History")

    response = requests.get(
        f"{base_url}/appointment_history/"
    )

    if response.status_code == 200:

        data = response.json()

        if len(data) > 0:
            st.dataframe(data)
        else:
            st.info("No past appointments found.")




with tab7:
    st.header("🎙️ Shifa AI Voice Assistant")

    st.success("Talk directly with Shifa AI by phone.")

    st.markdown("""
    ### How to Use

    1. Call the number below.
    2. Wait for Shifa AI to answer.
    3. Speak naturally.
    4. You can:
       - Book appointments
       - Check doctor availability
       - Reschedule appointments
       - Cancel appointments
    """)

    st.info("📞 Shifa AI Number: +1 (209) 880-3382")

    st.markdown("""
    ### Example Commands

    • Book an appointment with Dr. Sharma tomorrow at 10 AM.

    • Check availability of Dr. Khan on Monday.

    • Reschedule my appointment to 3 PM.

    • Cancel my appointment for tomorrow.
    """)

    st.markdown(
        """
        <a href="tel:+12098803382">
            <button style="
                background-color:#4CAF50;
                color:white;
                padding:15px 30px;
                border:none;
                border-radius:10px;
                font-size:18px;
                cursor:pointer;">
                📞 Call Shifa AI
            </button>
        </a>
        """,
        unsafe_allow_html=True
    )


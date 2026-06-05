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

    st.header("Shifa AI Assistant")

    st.write("Use your Vapi Assistant ID and Public Key to connect Shifa directly from this frontend.")

    # Use internal Vapi credentials (not entered by the user)
    # Replace these with secure retrieval (e.g., environment variables) as needed
    vapi_assistant_id = "aa9c10da-7172-4846-92e9-f09e234ccff6"
    vapi_public_key = "82442028-3271-4550-8c58-d984617b36a3"

    shifa_message = st.text_area(
        "Message to Shifa",
        "",
        height=150
    )

    # Button to send message manually
    if st.button("Send to Shifa", key="shifa_send"):

        if not shifa_message.strip():
            st.warning("Please enter a message for Shifa.")
        elif not vapi_assistant_id.strip() or not vapi_public_key.strip():
            st.warning("Please enter your Vapi Assistant ID and Public Key.")
        else:
            payload = {
                "message": shifa_message,
                "assistant_id": vapi_assistant_id,
                "public_key": vapi_public_key
            }

            response = requests.post(
                f"{base_url}/shifa_agent/",
                json=payload
            )

            if response.status_code == 200:
                reply = response.json().get("reply")
                if reply:
                    st.success("Shifa says:")
                    st.write(reply)
                else:
                    st.info(response.json())
            else:
                st.error(response.text)
    # Additional button labeled "Logo" which also sends the same payload when clicked
    if st.button("Logo", key="logo_button"):
        if not shifa_message.strip():
            st.warning("Please enter a message for Shifa.")
        else:
            payload = {
                "message": shifa_message,
                "assistant_id": vapi_assistant_id,
                "public_key": vapi_public_key
            }

            response = requests.post(
                f"{base_url}/shifa_agent/",
                json=payload
            )

            if response.status_code == 200:
                reply = response.json().get("reply")
                if reply:
                    st.success("Shifa says:")
                    st.write(reply)
                else:
                    st.info(response.json())
            else:
                st.error(response.text)



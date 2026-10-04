# import streamlit as st
# import datetime as dt
# import requests

# st.set_page_config(
#     page_title="Hospital Appointment System",
#     page_icon="🏥",
#     layout="wide"
# )

# st.title("🏥 Hospital Appointment System")

# base_url = st.text_input("Backend URL", "https://ai-hospital-appointment-voice-agent.onrender.com").rstrip("/")

# # patient_name = st.text_input("Patient Name")
# # reason = st.text_input("Reason for Appointment")
# # start_time = st.time_input("Time", value=dt.time(9,0))
# # start_date = st.date_input("Date", value=dt.date.today() + dt.timedelta(days=1))



# tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(
#     [
#         "Book Appointment",
#         "Check Availability",
#         "Reschedule",
#         "Cancel",
#         "List Appointments",
#         "History",
#         "Shifa Assistant"
#     ]
# )

# # ==========================
# # BOOK APPOINTMENT
# # ==========================

# with tab1:

#     st.header("Book Appointment")

#     patient_name = st.text_input("Patient Name")

#     reason = st.text_input("Reason")

#     appointment_date = st.date_input(
#         "Appointment Date",
#         value=dt.date.today()
#     )

#     appointment_time = st.time_input(
#         "Appointment Time",
#         value=dt.time(9, 0)
#     )

#     if st.button("Book Appointment"):

#         start_datetime = dt.datetime.combine(
#             appointment_date,
#             appointment_time
#         )

#         payload = {
#             "patient_name": patient_name,
#             "reason": reason,
#             "start_time": start_datetime.isoformat()
#         }

#         response = requests.post(
#             f"{base_url}/book_appointments/",
#             json=payload
#         )

#         if response.status_code == 200:
#             st.success("Appointment booked successfully")
#             st.json(response.json())
#         else:
#             st.error(response.text)

# # ==========================
# # CHECK AVAILABILITY
# # ==========================

# with tab2:

#     st.header("Check Availability")

#     check_date = st.date_input(
#         "Date",
#         value=dt.date.today(),
#         key="check_date"
#     )

#     check_time = st.time_input(
#         "Time",
#         value=dt.time(9, 0),
#         key="check_time"
#     )

#     if st.button("Check Availability"):

#         payload = {
#             "date": str(check_date),
#             "start_time": str(check_time)
#         }

#         response = requests.post(
#             f"{base_url}/check_availability/",
#             json=payload
#         )

#         if response.status_code == 200:

#             available = response.json()["available"]

#             if available:
#                 st.success("Slot Available")
#             else:
#                 st.warning("Slot Not Available")

#         else:
#             st.error(response.text)

# # ==========================
# # RESCHEDULE
# # ==========================

# with tab3:

#     st.header("Reschedule Appointment")

#     appointment_id = st.number_input(
#         "Appointment ID",
#         min_value=1,
#         step=1
#     )

#     new_date = st.date_input(
#         "New Date",
#         key="new_date"
#     )

#     new_time = st.time_input(
#         "New Time",
#         key="new_time"
#     )

#     if st.button("Reschedule"):

#         payload = {
#             "appointment_id": int(appointment_id),
#             "start_time": dt.datetime.combine(
#                 new_date,
#                 new_time
#             ).isoformat()
#         }

#         response = requests.post(
#             f"{base_url}/reschedule_appointments/",
#             json=payload
#         )

#         if response.status_code == 200:
#             st.success("Appointment Rescheduled")
#             st.json(response.json())
#         else:
#             st.error(response.text)

# # ==========================
# # CANCEL
# # ==========================

# with tab4:

#     st.header("Cancel Appointment")

#     cancel_id = st.number_input(
#         "Appointment ID",
#         min_value=1,
#         step=1,
#         key="cancel_id"
#     )

#     cancel_name = st.text_input(
#         "Patient Name",
#         key="cancel_name"
#     )


#     if st.button("Cancel Appointment"):

#         payload = {
#             "appointment_id": int(cancel_id),
#             "patient_name": cancel_name,
#         }

#         response = requests.post(
#             f"{base_url}/cancel_appointments/",
#             json=payload
#         )

#         if response.status_code == 200:
#             st.success("Appointment Cancelled")
#             st.json(response.json())
#         else:
#             st.error(response.text)

# # ==========================
# # LIST APPOINTMENTS
# # ==========================

# with tab5:

#     st.header("List Appointments")

#     search_date = st.date_input(
#         "Date",
#         value=dt.date.today()
#     )

#     if st.button("Load Appointments"):

#         payload = {
#             "date": str(search_date)
#         }

#         response = requests.post(
#             f"{base_url}/list_appointments/",
#             json=payload
#         )

#         if response.status_code == 200:

#             appointments = response.json()["appointments"]

#             if len(appointments) == 0:
#                 st.info("No appointments found")
#             else:
#                 st.dataframe(appointments)

#         else:
#             st.error(response.text)


# with tab6:

#     st.header("Appointment History")

#     response = requests.get(
#         f"{base_url}/appointment_history/"
#     )

#     if response.status_code == 200:

#         data = response.json()

#         if len(data) > 0:
#             st.dataframe(data)
#         else:
#             st.info("No past appointments found.")




# with tab7:
#     st.header("🎙️ Call Shifa AI")

#     phone_number = st.text_input(
#         "Enter your phone number",
#         placeholder="+919876543210"
#     )

#     if st.button("📞 Connect Me to Shifa AI"):

#         payload = {
#             "phone_number": phone_number
#         }

#         response = requests.post(
#             f"{base_url}/call_shifa/",
#             json=payload
#         )

#         if response.status_code == 200:
#             st.success(
#                 "You will receive a call from Shifa AI shortly."
#             )
#         else:
#             st.error(response.text)


# import streamlit as st
# import datetime as dt
# import requests
# import pandas as pd

# # ==========================================
# # PAGE CONFIGURATION & MEDICAL THEME SETUP
# # ==========================================
# st.set_page_config(
#     page_title="AI-Based Hospital Appointment System",
#     page_icon="🏥",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# # Custom CSS styling matching the exact reference dashboard colors, cards, and status badges
# st.markdown("""
#     <style>
#     /* Global background & text styling */
#     .main {
#         background-color: #F8FAFC;
#         color: #1E293B;
#         font-family: 'Inter', sans-serif;
#     }
    
#     /* Deep Royal Blue Sidebar matching reference image */
#     [data-testid="stSidebar"] {
#         background-color: #0B2545;
#         color: #FFFFFF;
#         border-right: none;
#     }
#     [data-testid="stSidebar"] .stRadio label {
#         color: #E2E8F0 !important;
#         font-weight: 500;
#         font-size: 15px;
#     }
#     [data-testid="stSidebar"] h3, [data-testid="stSidebar"] p, [data-testid="stSidebar"] span {
#         color: #FFFFFF !important;
#     }

#     /* Hero Banner matching reference image */
#     .hero-banner {
#         background: linear-gradient(135deg, #E0F2FE 0%, #BAE6FD 100%);
#         padding: 28px 32px;
#         border-radius: 14px;
#         border: 1px solid #7DD3FC;
#         margin-bottom: 24px;
#         box-shadow: 0 4px 12px rgba(0, 119, 182, 0.05);
#     }

#     /* Standardized Card Styling */
#     .dashboard-card {
#         background-color: #FFFFFF;
#         border: 1px solid #E2E8F0;
#         padding: 20px;
#         border-radius: 12px;
#         box-shadow: 0 2px 4px rgba(0, 0, 0, 0.02);
#         height: 100%;
#     }

#     /* Metric Cards with Individual Accent Colors from Reference */
#     .metric-card-1 {
#         background-color: #F0F9FF;
#         border: 1px solid #BAE6FD;
#         border-left: 5px solid #0077B6;
#         padding: 18px;
#         border-radius: 10px;
#     }
#     .metric-card-2 {
#         background-color: #F0FDF4;
#         border: 1px solid #BBF7D0;
#         border-left: 5px solid #16A34A;
#         padding: 18px;
#         border-radius: 10px;
#     }
#     .metric-card-3 {
#         background-color: #F0FDFA;
#         border: 1px solid #99F6E4;
#         border-left: 5px solid #0D9488;
#         padding: 18px;
#         border-radius: 10px;
#     }
#     .metric-card-4 {
#         background-color: #FEF2F2;
#         border: 1px solid #FECACA;
#         border-left: 5px solid #DC2626;
#         padding: 18px;
#         border-radius: 10px;
#     }

#     /* Status Badges */
#     .badge-confirmed {
#         background-color: #DCFCE7;
#         color: #15803D;
#         padding: 4px 10px;
#         border-radius: 12px;
#         font-weight: 600;
#         font-size: 12px;
#     }
#     .badge-pending {
#         background-color: #FEF9C3;
#         color: #A16207;
#         padding: 4px 10px;
#         border-radius: 12px;
#         font-weight: 600;
#         font-size: 12px;
#     }

#     /* Primary Buttons */
#     .stButton button {
#         background-color: #0077B6;
#         color: white;
#         border-radius: 8px;
#         font-weight: 600;
#         border: none;
#         padding: 0.5rem 1rem;
#         box-shadow: 0 2px 4px rgba(0, 119, 182, 0.2);
#         transition: all 0.2s ease;
#     }
#     .stButton button:hover {
#         background-color: #023E8A;
#         color: white;
#     }

#     h1, h2, h3, h4 {
#         color: #0B2545;
#     }
#     </style>
# """, unsafe_allow_html=True)

# # ==========================================
# # SIDEBAR NAVIGATION
# # ==========================================
# st.sidebar.markdown("### 🏥 Al Hospital")
# st.sidebar.caption("Appointment System")
# st.sidebar.markdown("---")

# menu = st.sidebar.radio(
#     "Navigation",
#     [
#         "🏠 Dashboard",
#         "📅 Book Appointment",
#         "📋 My Appointments",
#         "🔄 Reschedule Appointment",
#         "❌ Cancel Appointment",
#         "🔍 Check Availability",
#         "🎙️ AI Voice Assistant",
#         "ℹ️ About System"
#     ]
# )

# st.sidebar.markdown("---")
# with st.sidebar.expander("⚙️ Backend Settings"):
#     base_url = st.text_input("Backend URL", value="https://ai-hospital-appointment-voice-agent.onrender.com").rstrip("/")

# st.sidebar.markdown("<br><br>", unsafe_allow_html=True)
# st.sidebar.markdown("""
#     <div style="text-align: center; color: #94A3B8; font-size: 12px;">
#         <p style="margin-bottom: 4px;">❤️ Better Health</p>
#         <p style="margin-top: 0;">Brighter Tomorrow</p>
#     </div>
# """, unsafe_allow_html=True)

# # Safe wrapper for backend API calls
# def safe_api_call(func):
#     try:
#         return func()
#     except requests.exceptions.ConnectionError:
#         st.error("❌ Unable to connect to the hospital server. Please make sure the FastAPI backend is running.")
#         return None
#     except requests.exceptions.Timeout:
#         st.error("⏳ The request timed out. Please try again.")
#         return None
#     except Exception as e:
#         st.error(f"⚠️ An unexpected error occurred: {str(e)}")
#         return None

# # ==========================================
# # 🏠 DASHBOARD VIEW (Reference Image Layout)
# # ==========================================
# if menu == "🏠 Dashboard":
#     # Top Header
#     col_top1, col_top2 = st.columns([7, 1])
#     with col_top2:
#         st.markdown("<div style='text-align: right; padding-top: 8px;'>🔔 &nbsp; <b>👤 Patient ▾</b></div>", unsafe_allow_html=True)

#     # Hero Banner
#     st.markdown("""
#         <div class="hero-banner">
#             <div style="display: flex; justify-content: space-between; align-items: center;">
#                 <div>
#                     <p style="color: #0284C7; font-weight: 600; margin-bottom: 4px; font-size: 14px;">Welcome to</p>
#                     <h2 style="color: #0B2545; margin-top: 0; margin-bottom: 8px; font-size: 26px;">AI-Based Hospital Appointment System</h2>
#                     <p style="color: #334155; font-size: 15px; margin-bottom: 0;">Smart, simple and AI-powered healthcare appointment management.</p>
#                 </div>
#             </div>
#         </div>
#     """, unsafe_allow_html=True)

#     # Fetch dynamic data from backend history
#     def fetch_history():
#         res = requests.get(f"{base_url}/appointment_history/", timeout=10)
#         if res.status_code == 200:
#             return res.json()
#         return []

#     history_data = safe_api_call(fetch_history) or []
#     total_appts = len(history_data)
    
#     confirmed_count = len([a for a in history_data if str(a.get("status", "")).lower() in ["confirmed", "active"]])
#     pending_count = len([a for a in history_data if str(a.get("status", "")).lower() in ["pending"]])
#     cancelled_count = len([a for a in history_data if str(a.get("status", "")).lower() in ["cancelled"]])

#     # 4 Colored Metric Cards Matching Reference Design[cite: 4]
#     m1, m2, m3, m4 = st.columns(4)
#     with m1:
#         st.markdown(f"""
#             <div class="metric-card-1">
#                 <p style="color: #64748B; font-size: 13px; font-weight: 600; margin: 0 0 6px 0;">Total Appointments</p>
#                 <h2 style="color: #0B2545; margin: 0; font-size: 28px;">{total_appts}</h2>
#                 <p style="color: #64748B; font-size: 11px; margin: 6px 0 0 0;">All time appointments</p>
#             </div>
#         """, unsafe_allow_html=True)
#     with m2:
#         st.markdown(f"""
#             <div class="metric-card-2">
#                 <p style="color: #64748B; font-size: 13px; font-weight: 600; margin: 0 0 6px 0;">Upcoming Appointments</p>
#                 <h2 style="color: #16A34A; margin: 0; font-size: 28px;">{confirmed_count + pending_count}</h2>
#                 <p style="color: #64748B; font-size: 11px; margin: 6px 0 0 0;">Next 7 days</p>
#             </div>
#         """, unsafe_allow_html=True)
#     with m3:
#         st.markdown(f"""
#             <div class="metric-card-3">
#                 <p style="color: #64748B; font-size: 13px; font-weight: 600; margin: 0 0 6px 0;">Confirmed Appointments</p>
#                 <h2 style="color: #0D9488; margin: 0; font-size: 28px;">{confirmed_count}</h2>
#                 <p style="color: #64748B; font-size: 11px; margin: 6px 0 0 0;">Active appointments</p>
#             </div>
#         """, unsafe_allow_html=True)
#     with m4:
#         st.markdown(f"""
#             <div class="metric-card-4">
#                 <p style="color: #64748B; font-size: 13px; font-weight: 600; margin: 0 0 6px 0;">Cancelled Appointments</p>
#                 <h2 style="color: #DC2626; margin: 0; font-size: 28px;">{cancelled_count}</h2>
#                 <p style="color: #64748B; font-size: 11px; margin: 6px 0 0 0;">Total cancelled</p>
#             </div>
#         """, unsafe_allow_html=True)

#     st.markdown("<br>", unsafe_allow_html=True)

#     # Middle Section: Upcoming Appointments Table & AI Voice Assistant Card
#     col_left, col_right = st.columns([2, 1])

#     with col_left:
#         st.markdown("""
#             <div class="dashboard-card">
#                 <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
#                     <h3 style="margin: 0; font-size: 18px;">📋 Upcoming Appointments</h3>
#                     <span style="color: #0077B6; font-size: 13px; font-weight: 600; cursor: pointer;">View All →</span>
#                 </div>
#         """, unsafe_allow_html=True)
        
#         if history_data:
#             table_rows = []
#             for idx, item in enumerate(history_data[:5]):
#                 status_val = str(item.get("status", "Confirmed"))
#                 table_rows.append({
#                     "ID": f"APT-{item.get('id', idx+1):03d}",
#                     "Patient Name": item.get("patient_name", "N/A"),
#                     "Reason": item.get("reason", "Consultation"),
#                     "Date": str(item.get("start_time", ""))[:10],
#                     "Time": str(item.get("start_time", ""))[11:16] if len(str(item.get("start_time", ""))) >= 16 else "10:00 AM",
#                     "Status": status_val
#                 })
            
#             df_display = pd.DataFrame(table_rows)
#             st.dataframe(df_display, use_container_width=True, hide_index=True)
#         else:
#             st.info("No appointment records found in the database.")
            
#         st.markdown("</div>", unsafe_allow_html=True)

#     with col_right:
#         st.markdown("""
#             <div class="dashboard-card">
#                 <h3 style="color: #0B2545; margin-top: 0; font-size: 18px;">🎙️ AI Voice Assistant</h3>
#                 <p style="color: #64748B; font-size: 13px;">Book and manage your appointments using our AI-powered voice assistant.</p>
#                 <hr style="border: none; border-top: 1px solid #E2E8F0; margin: 12px 0;">
#                 <p style="font-weight: 600; color: #1E293B; font-size: 13px;">The AI assistant can help you:</p>
#                 <ul style="color: #334155; font-size: 13px; padding-left: 18px; line-height: 1.5; margin-bottom: 15px;">
#                     <li>Book appointments</li>
#                     <li>Check availability</li>
#                     <li>Reschedule appointments</li>
#                     <li>Cancel appointments</li>
#                     <li>Check appointment information</li>
#                 </ul>
#             </div>
#         """, unsafe_allow_html=True)
        
#         dashboard_phone = st.text_input("Enter phone for AI Call", placeholder="+919876543210", key="dash_phone", label_visibility="collapsed")
#         if st.button("🎙️ Start Voice Assistant", use_container_width=True):
#             if not dashboard_phone:
#                 st.warning("Please enter a phone number.")
#             else:
#                 def call_vapi():
#                     return requests.post(f"{base_url}/call_shifa/", json={"phone_number": dashboard_phone}, timeout=10)
#                 res = safe_api_call(call_vapi)
#                 if res and res.status_code == 200:
#                     st.success("📞 Call initiated successfully!")

#     st.markdown("<br>", unsafe_allow_html=True)

#     # Bottom Row: Quick Actions, Appointment Status, Need Help
#     b1, b2, b3 = st.columns(3)
#     with b1:
#         st.markdown("""
#             <div class="dashboard-card">
#                 <h4 style="margin-top: 0; margin-bottom: 15px;">Quick Actions</h4>
#             </div>
#         """, unsafe_allow_html=True)
#         if st.button("📅 Book Appointments", use_container_width=True):
#             st.info("Switch to 'Book Appointment' in the sidebar.")
#         if st.button("🔍 Check Availability", use_container_width=True):
#             st.info("Switch to 'Check Availability' in the sidebar.")
#         if st.button("🎙️ AI Voice Assistant", use_container_width=True):
#             st.info("Switch to 'AI Voice Assistant' in the sidebar.")

#     with b2:
#         st.markdown(f"""
#             <div class="dashboard-card">
#                 <h4 style="margin-top: 0; margin-bottom: 10px;">Appointment Status</h4>
#                 <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 15px;">
#                     <div>
#                         <p style="margin: 6px 0; font-size: 13px;">🟢 Confirmed: <b>{confirmed_count}</b></p>
#                         <p style="margin: 6px 0; font-size: 13px;">🟡 Pending: <b>{pending_count}</b></p>
#                         <p style="margin: 6px 0; font-size: 13px;">🔴 Cancelled: <b>{cancelled_count}</b></p>
#                     </div>
#                     <div style="text-align: center; background: #F8FAFC; padding: 12px 18px; border-radius: 10px; border: 1px solid #E2E8F0;">
#                         <span style="font-size: 24px; font-weight: bold; color: #0B2545;">{total_appts}</span><br>
#                         <span style="font-size: 11px; color: #64748B; font-weight: 600;">Total</span>
#                     </div>
#                 </div>
#             </div>
#         """, unsafe_allow_html=True)

#     with b3:
#         st.markdown("""
#             <div class="dashboard-card">
#                 <h4 style="margin-top: 0; margin-bottom: 8px;">🏥 Need Help?</h4>
#                 <p style="color: #64748B; font-size: 13px; margin-bottom: 12px;">Use our AI voice assistant for quick and easy appointment booking.</p>
#                 <div style="background: #E0F2FE; padding: 12px; border-radius: 8px; text-align: center; border: 1px solid #BAE6FD;">
#                     <p style="color: #0369A1; font-weight: 700; font-size: 13px; margin: 0;">🎧 Speak • Book • Manage</p>
#                     <p style="color: #334155; font-size: 11px; margin: 2px 0 0 0;">Your hospital assistant is always here!</p>
#                 </div>
#             </div>
#         """, unsafe_allow_html=True)

# # ==========================================
# # 📅 BOOK APPOINTMENT
# # ==========================================
# elif menu == "📅 Book Appointment":
#     st.header("📅 Book Appointment")
#     st.caption("Fill in patient details to book a consultation slot.")
#     st.markdown("---")

#     with st.form("booking_form"):
#         patient_name = st.text_input("Patient Name")
#         reason = st.text_input("Reason")

#         col1, col2 = st.columns(2)
#         with col1:
#             appointment_date = st.date_input("Appointment Date", value=dt.date.today())
#         with col2:
#             appointment_time = st.time_input("Appointment Time", value=dt.time(9, 0))

#         submitted = st.form_submit_button("Book Appointment")

#         if submitted:
#             if not patient_name or not reason:
#                 st.warning("⚠️ Please provide both Patient Name and Reason.")
#             else:
#                 start_datetime = dt.datetime.combine(appointment_date, appointment_time)
#                 payload = {
#                     "patient_name": patient_name,
#                     "reason": reason,
#                     "start_time": start_datetime.isoformat()
#                 }

#                 def call_book():
#                     return requests.post(f"{base_url}/book_appointments/", json=payload, timeout=10)

#                 response = safe_api_call(call_book)
#                 if response:
#                     if response.status_code == 200:
#                         st.success("✅ Appointment booked successfully")
#                         st.json(response.json())
#                     else:
#                         st.error(response.text)

# # ==========================================
# # 📋 MY APPOINTMENTS
# # ==========================================
# elif menu == "📋 My Appointments":
#     st.header("📋 My Appointments")
#     st.caption("Retrieve scheduled appointments for a specific date.")
#     st.markdown("---")

#     search_date = st.date_input("Date", value=dt.date.today())

#     if st.button("Load Appointments"):
#         payload = {"date": str(search_date)}

#         def call_list():
#             return requests.post(f"{base_url}/list_appointments/", json=payload, timeout=10)

#         response = safe_api_call(call_list)
#         if response:
#             if response.status_code == 200:
#                 appointments = response.json().get("appointments", [])
#                 if len(appointments) == 0:
#                     st.info("No appointments found")
#                 else:
#                     st.dataframe(appointments, use_container_width=True)
#             else:
#                 st.error(response.text)

# # ==========================================
# # 🔄 RESCHEDULE APPOINTMENT
# # ==========================================
# elif menu == "🔄 Reschedule Appointment":
#     st.header("🔄 Reschedule Appointment")
#     st.caption("Update schedule details for an active appointment ID.")
#     st.markdown("---")

#     with st.form("reschedule_form"):
#         appointment_id = st.number_input("Appointment ID", min_value=1, step=1)

#         col1, col2 = st.columns(2)
#         with col1:
#             new_date = st.date_input("New Date", key="new_date")
#         with col2:
#             new_time = st.time_input("New Time", key="new_time")

#         reschedule_submitted = st.form_submit_button("Reschedule")

#         if reschedule_submitted:
#             payload = {
#                 "appointment_id": int(appointment_id),
#                 "start_time": dt.datetime.combine(new_date, new_time).isoformat()
#             }

#             def call_resched():
#                 return requests.post(f"{base_url}/reschedule_appointments/", json=payload, timeout=10)

#             response = safe_api_call(call_resched)
#             if response:
#                 if response.status_code == 200:
#                     st.success("✅ Appointment Rescheduled")
#                     st.json(response.json())
#                 else:
#                     st.error(response.text)

# # ==========================================
# # ❌ CANCEL APPOINTMENT
# # ==========================================
# elif menu == "❌ Cancel Appointment":
#     st.header("❌ Cancel Appointment")
#     st.caption("Safely cancel an appointment using verification details.")
#     st.markdown("---")

#     with st.form("cancel_form"):
#         cancel_id = st.number_input("Appointment ID", min_value=1, step=1, key="cancel_id")
#         cancel_name = st.text_input("Patient Name", key="cancel_name")

#         st.warning("⚠️ Are you sure you want to cancel this appointment?")
#         cancel_submitted = st.form_submit_button("Cancel Appointment")

#         if cancel_submitted:
#             if not cancel_name:
#                 st.warning("Please provide the patient name for verification.")
#             else:
#                 payload = {
#                     "appointment_id": int(cancel_id),
#                     "patient_name": cancel_name,
#                 }

#                 def call_cancel():
#                     return requests.post(f"{base_url}/cancel_appointments/", json=payload, timeout=10)

#                 response = safe_api_call(call_cancel)
#                 if response:
#                     if response.status_code == 200:
#                         st.success("✅ Appointment Cancelled")
#                         st.json(response.json())
#                     else:
#                         st.error(response.text)

# # ==========================================
# # 🔍 CHECK AVAILABILITY
# # ==========================================
# elif menu == "🔍 Check Availability":
#     st.header("🔍 Check Availability")
#     st.caption("Verify if a specific date and time slot is open.")
#     st.markdown("---")

#     col1, col2 = st.columns(2)
#     with col1:
#         check_date = st.date_input("Date", value=dt.date.today(), key="check_date")
#     with col2:
#         check_time = st.time_input("Time", value=dt.time(9, 0), key="check_time")

#     if st.button("Check Availability"):
#         payload = {
#             "date": str(check_date),
#             "start_time": str(check_time)
#         }

#         def call_avail():
#             return requests.post(f"{base_url}/check_availability/", json=payload, timeout=10)

#         response = safe_api_call(call_avail)
#         if response:
#             if response.status_code == 200:
#                 available = response.json().get("available", False)
#                 if available:
#                     st.success("✅ Slot Available")
#                 else:
#                     st.warning("⚠️️ Slot Not Available")
#             else:
#                 st.error(response.text)

# # ==========================================
# # 🎙️ AI VOICE ASSISTANT (Dedicated View)
# # ==========================================
# elif menu == "🎙️ AI Voice Assistant":
#     st.header("🎙️ Call Shifa AI Assistant")
#     st.caption("Connect instantly with our conversational voice agent powered by Vapi.")
#     st.markdown("---")

#     st.info("💡 Enter your phone number below to receive an automated voice call from Shifa AI to manage your bookings interactively.")

#     with st.container():
#         phone_number = st.text_input("Enter your phone number", placeholder="+919876543210")

#         if st.button("📞 Connect Me to Shifa AI"):
#             if not phone_number:
#                 st.warning("Please enter a valid phone number.")
#             else:
            
#                 payload = {"phone_number": phone_number}

#                 def call_shifa():
#                     return requests.post(f"{base_url}/call_shifa/", json=payload, timeout=10)

#                 response = safe_api_call(call_shifa)
#                 if response:
#                     if response.status_code == 200:
#                         st.success("📞 You will receive a call from Shifa AI shortly.")
#                     else:
#                         st.error(response.text)

# # ==========================================
# # ℹ️ ABOUT SYSTEM
# # ==========================================
# elif menu == "ℹ️ About System":
#     st.header("ℹ️ About System")
#     st.caption("MCA Final-Year Project Documentation")
#     st.markdown("---")

#     col1, col2 = st.columns(2)
#     with col1:
#         st.subheader("🏥 Project Scope")
#         st.write(
#             "The **AI-Based Hospital Appointment System** integrates a modern Streamlit frontend "
#             "with a FastAPI backend, PostgreSQL database, and Vapi AI voice agent for automated scheduling."
#         )
#     with col2:
#         st.subheader("🛠️ Technology Stack")
#         st.markdown("""
#         * **Frontend:** Streamlit
#         * **Backend:** FastAPI
#         * **Database:** PostgreSQL & SQLAlchemy
#         * **Voice AI:** Vapi AI (Shifa)
#         """)


import streamlit as st
import datetime as dt
import requests
import pandas as pd
from streamlit_option_menu import option_menu

# ==========================================
# PAGE CONFIGURATION & BOOTSTRAP INJECT
# ==========================================
st.set_page_config(
    page_title="AI-Based Hospital Appointment System",
    page_icon="hospital",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Inject Bootstrap Icons CDN and Custom Healthcare SaaS Styling

st.markdown("""
<link rel="stylesheet"
      href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
""", unsafe_allow_html=True)


# st.markdown("""
#     <style>
  


#     .main {
#         background-color: #F5F9FD;
#         color: #102A43;
#         font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
#     }
    
    
#     /* ==========================================
#      HOSPITAL SIDEBAR
#     ========================================== */

#     [data-testid="stSidebar"] {
#         background: #0B1F33 !important;
#         border-right: 1px solid rgba(255, 255, 255, 0.06);
#     }


#     /* Sidebar inner area */

#     [data-testid="stSidebar"] > div:first-child {
#         background: #0B1F33 !important;
#     }


#     /* ==========================================
#         HOSPITAL LOGO
#         ========================================== */

#     .sidebar-title-container {
#         display: flex;
#         align-items: center;
#         gap: 12px;
#         padding: 18px 10px 24px 10px;
#     }

#     .hospital-logo {
#         width: 42px;
#         height: 42px;
#         display: flex;
#         align-items: center;
#         justify-content: center;
#         background: #1769AA;
#         color: #FFFFFF;
#         border-radius: 11px;
#         font-size: 21px;
#         box-shadow:0 5px 15px rgba(23, 105, 170, 0.30);
#     }


# /* ==========================================
#    SIDEBAR TITLE
#    ========================================== */

#     .sidebar-title {
#         font-size: 20px;
#         font-weight: 700;
#         color: #FFFFFF;
#         line-height: 1.2;
#     }

#     .sidebar-subtitle {
#         margin-top: 3px;
#         font-size: 11px;
#         color: #8FB8D8;
#     }


# /* ==========================================
#    SIDEBAR DIVIDER
#    ========================================== */

#     [data-testid="stSidebar"] hr {
#         border-color: rgba(255, 255, 255, 0.08);
#     }


#     /* ==========================================
#        OPTION MENU
#     ========================================== */

#     [data-testid="stSidebar"] .nav-link {
#         transition:background-color 0.2s ease,
#         color 0.2s ease,
#         transform 0.2s ease;
#     }


#     /* Hover */

#     [data-testid="stSidebar"] .nav-link:hover {
#             background-color: #143A5A !important;
#             color: #FFFFFF !important;
#         }


#     /* Selected item */

#     [data-testid="stSidebar"] .nav-link-selected {
#         background: linear-gradient(90deg,#1769AA,#168AAD) !important;
#         color: #FFFFFF !important;
#         box-shadow:0 5px 14px rgba(23, 105, 170, 0.25);
#     }


#     /* Selected icon */

#     [data-testid="stSidebar"] .nav-link-selected i {
#             color: #FFFFFF !important;
#     }


#     /* Normal icons */

#     [data-testid="stSidebar"] .nav-link i {
#             margin-right: 8px;
#     }


# /* ==========================================
#    SIDEBAR BOTTOM STATUS
#    ========================================== */

#     .sidebar-status {
#         margin-top: 25px;
#         padding: 12px;
#         background: rgba(255, 255, 255, 0.04);
#         border: 1px solid rgba(255, 255, 255, 0.06);
#         border-radius: 10px;
#         color: #B8C9D8;
#         font-size: 12px;
#     }

#     .sidebar-status-dot {
#         display: inline-block;
#         width: 8px;
#         height: 8px;
#         background: #2ECC71;
#         border-radius: 50%;
#         margin-right: 7px;
#     }

    
#     .hero-banner {
#         background: linear-gradient(135deg, #EAF4FF 0%, #D0E3FF 100%);
#         padding: 32px;
#         border-radius: 16px;
#         border: 1px solid #BAE6FD;
#         margin-bottom: 24px;
#         box-shadow: 0 4px 16px rgba(22, 119, 255, 0.08);
#     }

    
#     .dashboard-card {
#         background-color: #FFFFFF;
#         border: 1px solid #E2E8F0;
#         padding: 20px;
#         border-radius: 12px;
#         box-shadow: 0 2px 6px rgba(16, 42, 67, 0.02);
#         height: 100%;
#     }

   
#     .kpi-card {
#         background-color: #FFFFFF;
#         border: 1px solid #E2E8F0;
#         border-left: 4px solid #1677FF;
#         padding: 20px;
#         border-radius: 10px;
#         box-shadow: 0 2px 4px rgba(0,0,0,0.02);
#     }
#     .kpi-card-green { border-left-color: #16A34A; }
#     .kpi-card-teal { border-left-color: #0F9D9A; }
#     .kpi-card-orange { border-left-color: #F59E0B; }
#     .kpi-card-red { border-left-color: #DC3545; }

    
#     .badge-confirmed {
#         background-color: #DCFCE7;
#         color: #15803D;
#         padding: 4px 10px;
#         border-radius: 12px;
#         font-weight: 600;
#         font-size: 12px;
#     }
#     .badge-pending {
#         background-color: #FEF9C3;
#         color: #A16207;
#         padding: 4px 10px;
#         border-radius: 12px;
#         font-weight: 600;
#         font-size: 12px;
#     }
#     .badge-cancelled {
#         background-color: #FEF2F2;
#         color: #DC2626;
#         padding: 4px 10px;
#         border-radius: 12px;
#         font-weight: 600;
#         font-size: 12px;
#     }

    
#     .stButton button {
#         background-color: #1677FF;
#         color: white;
#         border-radius: 8px;
#         font-weight: 600;
#         border: none;
#         padding: 0.5rem 1rem;
#         box-shadow: 0 2px 4px rgba(22, 119, 255, 0.2);
#         transition: all 0.2s ease;
#     }
#     .stButton button:hover {
#         background-color: #0958D9;
#         color: white;
#     }

#     h1, h2, h3, h4 {
#         color: #0B2A4A;
#     }

#     </style>""", unsafe_allow_html=True)

st.markdown("""
<style>

/* =========================================================
   GLOBAL APPLICATION THEME
   ========================================================= */

.stApp {
    background-color: #F5F9FD;
    color: #102A43;
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
}

.main {
    background-color: #F5F9FD;
    color: #102A43;
}


/* Main content spacing */

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1450px;
}


/* =========================================================
   HOSPITAL SIDEBAR
   ========================================================= */

[data-testid="stSidebar"] {
    background: #0B1F33 !important;
    border-right: 1px solid rgba(255, 255, 255, 0.06);
}

[data-testid="stSidebar"] > div:first-child {
    background: #0B1F33 !important;
}


/* =========================================================
   HOSPITAL LOGO
   ========================================================= */

.sidebar-title-container {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 18px 10px 24px 10px;
}

.hospital-logo {
    width: 42px;
    height: 42px;

    display: flex;
    align-items: center;
    justify-content: center;

    background: linear-gradient(
        135deg,
        #1769AA,
        #168AAD
    );

    color: #FFFFFF;

    border-radius: 11px;

    font-size: 21px;

    box-shadow:
        0 5px 15px rgba(23, 105, 170, 0.30);
}


/* =========================================================
   SIDEBAR TITLE
   ========================================================= */

.sidebar-title {
    font-size: 20px;
    font-weight: 700;
    color: #FFFFFF;
    line-height: 1.2;
}

.sidebar-subtitle {
    margin-top: 3px;
    font-size: 11px;
    color: #8FB8D8;
}


/* =========================================================
   SIDEBAR DIVIDER
   ========================================================= */

[data-testid="stSidebar"] hr {
    border-color: rgba(255, 255, 255, 0.08);
}


/* =========================================================
   OPTION MENU
   ========================================================= */

[data-testid="stSidebar"] .nav-link {

    font-size: 14px !important;

    font-weight: 500 !important;

    padding: 11px 14px !important;

    margin: 5px 0 !important;

    border-radius: 10px !important;

    color: #B8C9D8 !important;

    transition:
        background-color 0.2s ease,
        color 0.2s ease,
        transform 0.2s ease;
}


/* Normal icon */

[data-testid="stSidebar"] .nav-link i {

    color: #8FB8D8 !important;

    font-size: 17px !important;

    margin-right: 8px !important;
}


/* Hover */

[data-testid="stSidebar"] .nav-link:hover {

    background-color: #143A5A !important;

    color: #FFFFFF !important;

    transform: translateX(2px);
}

[data-testid="stSidebar"] .nav-link:hover i {

    color: #FFFFFF !important;
}


/* Selected */

[data-testid="stSidebar"] .nav-link-selected {

    background: linear-gradient(
        90deg,
        #1769AA,
        #168AAD
    ) !important;

    color: #FFFFFF !important;

    font-weight: 600 !important;

    box-shadow:
        0 5px 14px rgba(23, 105, 170, 0.25);
}

[data-testid="stSidebar"] .nav-link-selected i {

    color: #FFFFFF !important;
}


/* =========================================================
   SIDEBAR STATUS
   ========================================================= */

.sidebar-status {

    margin-top: 25px;

    padding: 12px;

    background: rgba(255, 255, 255, 0.04);

    border:
        1px solid rgba(255, 255, 255, 0.06);

    border-radius: 10px;

    color: #B8C9D8;

    font-size: 12px;
}

.sidebar-status-dot {

    display: inline-block;

    width: 8px;
    height: 8px;

    background: #2ECC71;

    border-radius: 50%;

    margin-right: 7px;
}


/* =========================================================
   PAGE HEADINGS
   ========================================================= */

h1 {
    color: #0B2A4A !important;
    font-size: 32px !important;
    font-weight: 750 !important;
}

h2 {
    color: #0B2A4A !important;
    font-weight: 700 !important;
}

h3 {
    color: #163A5F !important;
    font-weight: 700 !important;
}

h4 {
    color: #163A5F !important;
    font-weight: 650 !important;
}


/* Normal text */

[data-testid="stMarkdownContainer"] p {

    color: #526579;

    line-height: 1.6;
}


/* =========================================================
   PAGE HEADER
   ========================================================= */

.page-header {

    margin-bottom: 24px;
}

.page-header-title {

    color: #0B2A4A;

    font-size: 30px;

    font-weight: 750;

    margin-bottom: 5px;
}

.page-header-subtitle {

    color: #6B7C93;

    font-size: 14px;

    margin-bottom: 18px;
}


/* =========================================
   DASHBOARD HERO SECTION
   ========================================= */

.hero-banner {
    position: relative;
    min-height: 285px;
    border-radius: 20px;
    overflow: hidden;

    background-image:
        linear-gradient(
            90deg,
            rgba(7, 30, 52, 0.94) 0%,
            rgba(10, 48, 78, 0.86) 45%,
            rgba(10, 48, 78, 0.45) 100%
        ),
        url("https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?auto=format&fit=crop&w=1400&q=85");

    background-size: cover;
    background-position: center;

    border: 1px solid #B8DDED;

    box-shadow:
        0 8px 25px rgba(16, 42, 67, 0.12);
}


/* Hero content wrapper */

.hero-overlay {
    min-height: 285px;

    display: flex;
    align-items: center;

    padding: 32px 38px;
}


/* Hero content */

.hero-content {
    max-width: 780px;
}


/* Badge */

.hero-badge {
    display: inline-flex;
    align-items: center;
    gap: 7px;

    padding: 7px 13px;

    background: rgba(255, 255, 255, 0.12);

    border: 1px solid rgba(255, 255, 255, 0.25);

    border-radius: 20px;

    color: #BDE7FF;

    font-size: 11px;
    font-weight: 700;
    letter-spacing: 0.6px;

    margin-bottom: 13px;

    backdrop-filter: blur(8px);
}

.hero-badge i {
    font-size: 13px;
}


/* Main heading */

.hero-title {
    color: #FFFFFF !important;

    font-size: 31px;
    font-weight: 750;

    line-height: 1.22;

    letter-spacing: -0.5px;

    margin-bottom: 12px;
}


/* Description */

.hero-description {
    color: #E2EDF5 !important;

    font-size: 14px;

    line-height: 1.7;

    max-width: 700px;

    margin-bottom: 18px;
}


/* Feature pills */

.hero-features {
    display: flex;
    flex-wrap: wrap;

    gap: 9px;
}

.hero-features span {
    display: inline-flex;
    align-items: center;

    gap: 6px;

    padding: 7px 11px;

    background: rgba(255, 255, 255, 0.10);

    border: 1px solid rgba(255, 255, 255, 0.18);

    border-radius: 20px;

    color: #FFFFFF;

    font-size: 11px;
    font-weight: 600;

    backdrop-filter: blur(6px);
}

.hero-features i {
    color: #6EE7B7;
    font-size: 12px;
}


/* =========================================
   CLINICAL EXCELLENCE CARD
   ========================================= */

.clinical-card {
    height: 100%;
    min-height: 285px;

    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;

    text-align: center;

    padding: 25px 20px;

    background: linear-gradient(
        145deg,
        #FFFFFF 0%,
        #F0F9FF 100%
    );

    border: 1px solid #BAE6FD;

    border-radius: 20px;

    box-shadow:
        0 8px 25px rgba(23, 105, 170, 0.08);
}


/* Hospital icon */

.clinical-icon {
    width: 58px;
    height: 58px;

    display: flex;
    align-items: center;
    justify-content: center;

    background: linear-gradient(
        135deg,
        #1769AA,
        #168AAD
    );

    color: #FFFFFF;

    border-radius: 16px;

    font-size: 25px;

    margin-bottom: 14px;

    box-shadow:
        0 7px 16px rgba(23, 105, 170, 0.22);
}


/* Card title */

.clinical-title {
    color: #0B2A4A !important;

    font-size: 17px;

    font-weight: 750;

    margin-bottom: 7px;
}


/* Card description */

.clinical-text {
    color: #64748B !important;

    font-size: 12px;

    line-height: 1.6;

    max-width: 210px;
}


/* Secure badge */

.secure-badge {
    display: inline-flex;
    align-items: center;

    margin-top: 16px;

    padding: 7px 11px;

    background: #ECFDF5;

    border: 1px solid #A7F3D0;

    border-radius: 20px;

    color: #047857;

    font-size: 10px;

    font-weight: 650;
}


.secure-dot {
    width: 7px;
    height: 7px;

    background: #10B981;

    border-radius: 50%;

    margin-right: 6px;

    box-shadow:
        0 0 0 3px rgba(16, 185, 129, 0.12);
}


/* Divider */

.clinical-divider {
    width: 80%;

    height: 1px;

    background: #E2E8F0;

    margin: 18px 0 12px;
}


/* Bottom information */

.clinical-bottom {
    display: flex;
    align-items: center;

    gap: 6px;

    color: #526579;

    font-size: 11px;

    font-weight: 600;
}

.clinical-bottom i {
    color: #1769AA;
    font-size: 13px;
}


/* =========================================================
   DASHBOARD CARDS
   ========================================================= */

.dashboard-card {

    background: #FFFFFF;

    border: 1px solid #E2E8F0;

    padding: 22px;

    border-radius: 14px;

    box-shadow:
        0 3px 12px rgba(16, 42, 67, 0.05);

    height: 100%;

    transition:
        transform 0.2s ease,
        box-shadow 0.2s ease;
}

.dashboard-card:hover {

    transform: translateY(-2px);

    box-shadow:
        0 8px 22px rgba(16, 42, 67, 0.08);
}


/* =========================================================
   KPI CARDS
   ========================================================= */

.kpi-card {

    background: #FFFFFF;

    border: 1px solid #E2E8F0;

    border-left: 5px solid #1769AA;

    padding: 20px;

    border-radius: 12px;

    min-height: 135px;

    box-shadow:
        0 3px 10px rgba(16, 42, 67, 0.05);

    transition:
        transform 0.2s ease,
        box-shadow 0.2s ease;
}

.kpi-card:hover {

    transform: translateY(-3px);

    box-shadow:
        0 8px 20px rgba(16, 42, 67, 0.09);
}

.kpi-card-green {
    border-left-color: #16A34A;
}

.kpi-card-teal {
    border-left-color: #0F9D9A;
}

.kpi-card-orange {
    border-left-color: #F59E0B;
}

.kpi-card-red {
    border-left-color: #DC3545;
}


/* KPI text */

.kpi-title {

    color: #526579;

    font-size: 13px;

    font-weight: 600;
}

.kpi-value {

    color: #102A43;

    font-size: 30px;

    font-weight: 750;

    margin-top: 6px;
}

.kpi-description {

    color: #829AB1;

    font-size: 12px;

    margin-top: 5px;
}


/* =========================================================
   APPOINTMENT CARDS
   ========================================================= */

.appointment-card {

    background: #FFFFFF;

    border: 1px solid #E2E8F0;

    border-radius: 12px;

    padding: 18px;

    margin-bottom: 12px;

    box-shadow:
        0 3px 10px rgba(16,42,67,0.04);

    transition:
        transform 0.2s ease,
        box-shadow 0.2s ease;
}

.appointment-card:hover {

    transform: translateY(-2px);

    box-shadow:
        0 7px 18px rgba(16,42,67,0.08);
}

.appointment-id {

    color: #1769AA;

    font-size: 12px;

    font-weight: 700;
}

.appointment-patient {

    color: #102A43;

    font-size: 18px;

    font-weight: 700;

    margin-top: 4px;
}

.appointment-info {

    color: #60758A;

    font-size: 13px;

    margin-top: 4px;
}


/* =========================================================
   FORM CARDS
   ========================================================= */

.form-card {

    background: #FFFFFF;

    border: 1px solid #E2E8F0;

    border-radius: 14px;

    padding: 25px;

    box-shadow:
        0 4px 15px rgba(16,42,67,0.05);

    margin-bottom: 20px;
}

.form-card-title {

    color: #102A43;

    font-size: 20px;

    font-weight: 700;

    margin-bottom: 5px;
}

.form-card-description {

    color: #6B7C93;

    font-size: 13px;

    margin-bottom: 20px;
}


/* =========================================================
   INPUTS
   ========================================================= */

.stTextInput input,
.stTextArea textarea,
.stNumberInput input,
.stDateInput input,
.stTimeInput input {

    background: #FFFFFF !important;

    color: #102A43 !important;

    border: 1px solid #CBD5E1 !important;

    border-radius: 8px !important;
}


/* Input labels */

label {

    color: #243B53 !important;

    font-weight: 600 !important;
}


/* Placeholder */

input::placeholder,
textarea::placeholder {

    color: #829AB1 !important;
}


/* Focus */

.stTextInput input:focus,
.stTextArea textarea:focus,
.stNumberInput input:focus {

    border-color: #1769AA !important;

    box-shadow:
        0 0 0 2px rgba(23,105,170,0.12) !important;
}


/* =========================================================
   SELECT BOX
   ========================================================= */

[data-baseweb="select"] > div {

    background: #FFFFFF !important;

    color: #102A43 !important;

    border-color: #CBD5E1 !important;

    border-radius: 8px !important;
}


/* =========================================================
   BUTTONS
   ========================================================= */

.stButton button {

    background:
        linear-gradient(
            135deg,
            #1769AA,
            #168AAD
        ) !important;

    color: #FFFFFF !important;

    border: none !important;

    border-radius: 8px !important;

    font-weight: 600 !important;

    padding: 0.55rem 1.1rem !important;

    box-shadow:
        0 3px 8px rgba(23,105,170,0.20);

    transition:
        all 0.2s ease;
}

.stButton button:hover {

    transform: translateY(-1px);

    box-shadow:
        0 6px 15px rgba(23,105,170,0.28);
}


/* =========================================================
   SECONDARY / ACTION BUTTONS
   ========================================================= */

.secondary-button {

    background: #EAF4FF;

    color: #1769AA;

    border: 1px solid #B9DDF5;

    border-radius: 8px;

    padding: 9px 16px;

    font-weight: 600;
}


/* =========================================================
   STATUS BADGES
   ========================================================= */

.badge-confirmed {

    background-color: #DCFCE7;

    color: #15803D;

    padding: 5px 11px;

    border-radius: 12px;

    font-weight: 600;

    font-size: 12px;
}

.badge-pending {

    background-color: #FEF9C3;

    color: #A16207;

    padding: 5px 11px;

    border-radius: 12px;

    font-weight: 600;

    font-size: 12px;
}

.badge-cancelled {

    background-color: #FEF2F2;

    color: #DC2626;

    padding: 5px 11px;

    border-radius: 12px;

    font-weight: 600;

    font-size: 12px;
}



/* ==========================================
   BOOK APPOINTMENT
   ========================================== */

.book-card {
    background: linear-gradient(
        135deg,
        #FFFFFF 0%,
        #F0FDF4 100%
    );

    border: 1px solid #BBF7D0;
    border-left: 5px solid #16A34A;

    border-radius: 15px;

    padding: 25px;

    margin-bottom: 22px;

    box-shadow: 0 5px 18px rgba(22, 163, 74, 0.08);
}

.book-icon {
    width: 48px;
    height: 48px;

    display: flex;
    align-items: center;
    justify-content: center;

    background: #DCFCE7;
    color: #16A34A;

    border-radius: 12px;

    font-size: 22px;

    margin-bottom: 12px;
}

.book-title {
    color: #166534 !important;

    font-size: 23px;
    font-weight: 750;

    margin-bottom: 6px;
}

.book-description {
    color: #475569 !important;

    font-size: 14px;
    line-height: 1.7;

    max-width: 850px;
}

.book-info {
    display: inline-flex;
    align-items: center;

    margin-top: 15px;

    padding: 7px 12px;

    background: #F0FDF4;
    border: 1px solid #BBF7D0;

    border-radius: 20px;

    color: #15803D;

    font-size: 12px;
    font-weight: 600;
}

.book-info i {
    margin-right: 6px;
}


.my-appointments-card {
    background: linear-gradient(
        135deg,
        #FFFFFF 0%,
        #F5F3FF 100%
    );
    border: 1px solid #DDD6FE;
    border-left: 5px solid #7C3AED;
    border-radius: 15px;
    padding: 25px;
    margin-bottom: 22px;
    box-shadow: 0 5px 18px rgba(124, 58, 237, 0.08);
}

.my-appointments-icon {
    width: 48px;
    height: 48px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: #EDE9FE;
    color: #7C3AED;
    border-radius: 12px;
    font-size: 22px;
    margin-bottom: 12px;
}

.my-appointments-title {
    color: #4C1D95 !important;
    font-size: 23px;
    font-weight: 750;
    margin-bottom: 6px;
}

.my-appointments-description {
    color: #475569 !important;
    font-size: 14px;
    line-height: 1.7;
    max-width: 850px;
}

.my-appointments-info {
    display: inline-flex;
    align-items: center;
    margin-top: 15px;
    padding: 7px 12px;
    background: #F5F3FF;
    border: 1px solid #DDD6FE;
    border-radius: 20px;
    color: #6D28D9;
    font-size: 12px;
    font-weight: 600;
}

.my-appointments-info i {
    margin-right: 6px;
}

/* ==========================================
   CANCEL APPOINTMENT
   ========================================== */

.cancel-card {
    background: linear-gradient(
        135deg,
        #FFFFFF 0%,
        #FFF5F5 100%
    );

    border: 1px solid #FECACA;
    border-left: 5px solid #DC3545;

    border-radius: 15px;

    padding: 25px;

    margin-bottom: 22px;

    box-shadow: 0 5px 18px rgba(220, 53, 69, 0.08);
}

.cancel-icon {
    width: 48px;
    height: 48px;

    display: flex;
    align-items: center;
    justify-content: center;

    background: #FEE2E2;
    color: #DC2626;

    border-radius: 12px;

    font-size: 22px;

    margin-bottom: 12px;
}

.cancel-title {
    color: #991B1B !important;

    font-size: 23px;
    font-weight: 750;

    margin-bottom: 6px;
}

.cancel-description {
    color: #7F1D1D !important;

    font-size: 14px;
    line-height: 1.7;
}


/* ==========================================
   RESCHEDULE APPOINTMENT
   ========================================== */

.reschedule-card {
    background: linear-gradient(
        135deg,
        #FFFFFF 0%,
        #F0F9FF 100%
    );

    border: 1px solid #BAE6FD;
    border-left: 5px solid #0284C7;

    border-radius: 15px;

    padding: 25px;

    margin-bottom: 22px;

    box-shadow: 0 5px 18px rgba(2, 132, 199, 0.08);
}

.reschedule-icon {
    width: 48px;
    height: 48px;

    display: flex;
    align-items: center;
    justify-content: center;

    background: #E0F2FE;
    color: #0284C7;

    border-radius: 12px;

    font-size: 22px;

    margin-bottom: 12px;
}

.reschedule-title {
    color: #075985 !important;

    font-size: 23px;
    font-weight: 750;

    margin-bottom: 6px;
}

.reschedule-description {
    color: #475569 !important;

    font-size: 14px;
    line-height: 1.7;
}


/* ==========================================
   CHECK AVAILABILITY
   ========================================== */

.availability-card {
    background: linear-gradient(
        135deg,
        #FFFFFF 0%,
        #F0FDFA 100%
    );

    border: 1px solid #99F6E4;
    border-left: 5px solid #0F9D9A;

    border-radius: 15px;

    padding: 25px;

    margin-bottom: 22px;

    box-shadow: 0 5px 18px rgba(15, 157, 154, 0.08);
}

.availability-icon {
    width: 48px;
    height: 48px;

    display: flex;
    align-items: center;
    justify-content: center;

    background: #CCFBF1;
    color: #0F766E;

    border-radius: 12px;

    font-size: 22px;

    margin-bottom: 12px;
}

.availability-title {
    color: #115E59 !important;

    font-size: 23px;
    font-weight: 750;

    margin-bottom: 6px;
}

.availability-description {
    color: #475569 !important;

    font-size: 14px;
    line-height: 1.7;
}


/* ==========================================
   AI VOICE ASSISTANT
   ========================================== */

.voice-card {
    background: linear-gradient(
        135deg,
        #FFFFFF 0%,
        #F3E8FF 100%
    );

    border: 1px solid #DDD6FE;
    border-left: 5px solid #7C3AED;

    border-radius: 15px;

    padding: 25px;

    margin-bottom: 22px;

    box-shadow: 0 5px 18px rgba(124, 58, 237, 0.10);
}

.voice-icon {
    width: 48px;
    height: 48px;

    display: flex;
    align-items: center;
    justify-content: center;

    background: #EDE9FE;
    color: #7C3AED;

    border-radius: 12px;

    font-size: 21px;

    margin-bottom: 12px;
}

.voice-title {
    color: #5B21B6 !important;

    font-size: 23px;
    font-weight: 750;

    margin-bottom: 6px;
}

.voice-description {
    color: #475569 !important;

    font-size: 14px;
    line-height: 1.7;

    max-width: 850px;
}

.voice-status {
    display: inline-flex;
    align-items: center;

    margin-top: 15px;

    padding: 7px 12px;

    background: #ECFDF5;
    border: 1px solid #A7F3D0;

    border-radius: 20px;

    color: #047857;

    font-size: 12px;
    font-weight: 600;
}

.voice-status-dot {
    width: 8px;
    height: 8px;

    background: #10B981;

    border-radius: 50%;

    margin-right: 7px;

    box-shadow: 0 0 0 3px rgba(16, 185, 129, 0.12);
}


/* ==========================================
   APPOINTMENT HISTORY
   ========================================== */

.history-card {
    background: linear-gradient(
        135deg,
        #FFFFFF 0%,
        #FFF7ED 100%
    );

    border: 1px solid #FED7AA;
    border-left: 5px solid #EA580C;

    border-radius: 15px;

    padding: 25px;

    margin-bottom: 22px;

    box-shadow: 0 5px 18px rgba(234, 88, 12, 0.08);
}

.history-icon {
    width: 48px;
    height: 48px;

    display: flex;
    align-items: center;
    justify-content: center;

    background: #FFEDD5;
    color: #EA580C;

    border-radius: 12px;

    font-size: 22px;

    margin-bottom: 12px;
}

.history-title {
    color: #9A3412 !important;

    font-size: 23px;
    font-weight: 750;

    margin-bottom: 6px;
}

.history-description {
    color: #475569 !important;

    font-size: 14px;
    line-height: 1.7;

    max-width: 850px;
}


/* Dataframe */

[data-testid="stDataFrame"] {

    border:
        1px solid #D9E2EC;

    border-radius: 10px;

    overflow: hidden;
}


.about-card {
    background: linear-gradient(
        135deg,
        #FFFFFF 0%,
        #EFF6FF 100%
    );
    border: 1px solid #BFDBFE;
    border-left: 5px solid #2563EB;
    border-radius: 15px;
    padding: 25px;
    margin-bottom: 22px;
    box-shadow: 0 5px 18px rgba(37, 99, 235, 0.08);
}

.about-icon {
    width: 48px;
    height: 48px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: #DBEAFE;
    color: #2563EB;
    border-radius: 12px;
    font-size: 22px;
    margin-bottom: 12px;
}

.about-title {
    color: #1E3A8A !important;
    font-size: 23px;
    font-weight: 750;
    margin-bottom: 6px;
}

.about-description {
    color: #475569 !important;
    font-size: 14px;
    line-height: 1.7;
    max-width: 900px;
}

.about-info {
    display: inline-flex;
    align-items: center;
    margin-top: 15px;
    padding: 7px 12px;
    background: #EFF6FF;
    border: 1px solid #BFDBFE;
    border-radius: 20px;
    color: #1D4ED8;
    font-size: 12px;
    font-weight: 600;
}

.about-info i {
    margin-right: 6px;
}


/* =========================================================
   ALERTS
   ========================================================= */

[data-testid="stAlert"] {

    border-radius: 10px !important;
}


/* =========================================================
   DIVIDERS
   ========================================================= */

hr {

    border-color: #D9E2EC !important;
}


/* =========================================================
   SCROLLBAR
   ========================================================= */

::-webkit-scrollbar {

    width: 8px;
}

::-webkit-scrollbar-track {

    background: #F1F5F9;
}

::-webkit-scrollbar-thumb {

    background: #B8C4D1;

    border-radius: 10px;
}

::-webkit-scrollbar-thumb:hover {

    background: #1769AA;
}


/* =========================================================
   MOBILE / SMALL SCREEN
   ========================================================= */

@media (max-width: 768px) {

    .block-container {

        padding: 1rem;
    }

    .hero-banner {

        padding: 20px;
    }

    .hero-title {

        font-size: 22px;
    }

    h1 {

        font-size: 26px !important;
    }
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# SIDEBAR NAVIGATION & BRANDING
# ==========================================



with st.sidebar:

    st.html("""
        <div class="sidebar-title-container">
            <div class="hospital-logo">
                <i class="bi bi-heart-pulse-fill"></i>
            </div>

            <div>
                <div class="sidebar-title">
                    AI Hospital
                </div>

                <div class="sidebar-subtitle">
                    Appointment System
                </div>
            </div>
        </div>""")

    selected_menu = option_menu(
        menu_title=None,

        options=[
            "Dashboard",
            "Book Appointment",
            "My Appointments",
            "Reschedule Appointment",
            "Cancel Appointment",
            "Check Availability",
            "AI Voice Assistant",
            "Appointment History",
            "About System"
        ],

        icons=[
            "speedometer2",
            "calendar-plus",
            "calendar-check",
            "arrow-repeat",
            "calendar-x",
            "search",
            "telephone",
            "clock-history",
            "info-circle"
        ],

        menu_icon="hospital",

        default_index=0,

        styles={
            "container": {
                "padding": "0!important",
                "background-color": "transparent"
            },

            "icon": {
                "color": "#8FB8D8",
                "font-size": "17px"
            },

            "nav-link": {
                "font-size": "14px",
                "font-weight": "500",
                "text-align": "left",
                "margin": "4px 0",
                "padding": "11px 14px",
                "border-radius": "10px",
                "color": "#B8C9D8",
                "--hover-color": "#173B5E"
            },

            "nav-link-selected": {
                "background-color": "#1769AA",
                "color": "#FFFFFF",
                "font-weight": "600",
                "box-shadow": "0 4px 12px rgba(23, 105, 170, 0.25)"
            }
          }
        )

st.sidebar.markdown("<br>", unsafe_allow_html=True)
with st.sidebar.expander("Backend Configuration"):
    base_url = st.text_input("FastAPI URL", value="https://ai-hospital-appointment-voice-agent.onrender.com").rstrip("/")

    if st.sidebar.button("Test Backend Connection"):
        try:
            response = requests.get(
            f"{base_url}/docs",
            timeout=30
            )

            if response.status_code == 200:
                st.sidebar.success("✅ FastAPI backend is connected!")
            else:
                st.sidebar.error(
                f"❌ Backend returned status code: {response.status_code}"
            )

        except requests.exceptions.Timeout:
            st.sidebar.error("❌ Backend request timed out.")

        except requests.exceptions.ConnectionError:
            st.sidebar.error("❌ Cannot connect to Render FastAPI.")

        except Exception as e:
            st.sidebar.error(f"❌ Error: {e}")

st.sidebar.markdown("<br><hr style='border-color: #1E3A5F;'>", unsafe_allow_html=True)
st.sidebar.markdown("""
    <div style="padding: 10px 0; font-size: 12px; color: #94A3B8;">
        <p style="margin: 0; font-weight: 600; color: #FFFFFF;"><i class="bi bi-robot" style="color: #0F9D9A;"></i> AI Assistant</p>
        <p style="margin: 2px 0;"><span style="color: #10B981; font-size: 16px;">●</span> Online • Voice service active</p>
        <p style="margin: 0; font-size: 11px;">Powered by Vapi AI</p>
    </div>
""", unsafe_allow_html=True)

# Safe API Handler
def safe_api_call(func):
    try:
        return func()
    except requests.exceptions.ConnectionError:
        st.error("Unable to connect to the hospital FastAPI server. Please ensure your backend is active.")
        return None
    except requests.exceptions.Timeout:
        st.error("The backend request timed out. Please try again.")
        return None
    except Exception as e:
        st.error(f"An unexpected error occurred: {str(e)}")
        return None

# ==========================================
# 1. DASHBOARD VIEW
# ==========================================
if selected_menu == "Dashboard":
    # Top Header
    h_col1, h_col2 = st.columns([7, 2])
    with h_col1:
        st.markdown("""
            <div style="display: flex; align-items: center; gap: 12px; background: #FFFFFF; padding: 10px 16px; border-radius: 8px; border: 1px solid #E2E8F0;">
                <i class="bi bi-search" style="color: #64748B;"></i>
                <span style="color: #94A3B8; font-size: 14px;">Search appointments, patients, doctors...</span>
            </div>
        """, unsafe_allow_html=True)
    with h_col2:
        st.markdown("""
            <div style="display: flex; justify-content: flex-end; align-items: center; gap: 16px; padding-top: 6px;">
                <i class="bi bi-bell" style="font-size: 18px; color: #64748B; cursor: pointer;"></i>
                <div style="display: flex; align-items: center; gap: 8px;">
                    <i class="bi bi-person-circle" style="font-size: 24px; color: #1677FF;"></i>
                    <div style="text-align: left; line-height: 1.2;">
                        <span style="font-size: 13px; font-weight: 600; color: #102A43; display: block;">Patient</span>
                        <span style="font-size: 11px; color: #64748B;">Welcome back!</span>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Hero Banner with Medical Background
    hero_col1, hero_col2 = st.columns([3, 1], gap="medium")

    with hero_col1:

        st.html("""
        <div class="hero-banner">

            <div class="hero-overlay">

                <div class="hero-content">

                    <div class="hero-badge">
                    <i class="bi bi-heart-pulse-fill"></i>
                    SMART HEALTHCARE PLATFORM
                    </div>

                    <div class="hero-title">
                        AI-Based Hospital<br>
                        Appointment System
                    </div>  

                    <div class="hero-description">
                    Smart, simple and AI-powered healthcare appointment
                    management designed for efficient clinical operations
                    and convenient patient services.
                    </div>

                    <div class="hero-features">

                        <span>
                        <i class="bi bi-check-circle-fill"></i>
                        Easy Booking
                        </span>

                        <span>
                        <i class="bi bi-check-circle-fill"></i>
                        Secure Management
                        </span>

                        <span>
                        <i class="bi bi-check-circle-fill"></i>
                        AI Assistance
                        </span>

                    </div>

                </div>

            </div>

        </div>
        """)

    with hero_col2:

        st.html("""
            <div class="clinical-card">

                <div class="clinical-icon">
                    <i class="bi bi-hospital-fill"></i>
                </div>

                <div class="clinical-title">
                    Clinical Excellence
                </div>

                <div class="clinical-text">
                Reliable and secure appointment
                management for modern healthcare.
                </div>

            <div class="secure-badge">
                <span class="secure-dot"></span>
                Verified Secure Portal
            </div>

            <div class="clinical-divider"></div>

            <div class="clinical-bottom">
            <i class="bi bi-shield-check"></i>
            Secure Healthcare
            </div>

        </div>
        """)

    # Fetch dynamic appointment history for KPIs
    def fetch_history():
        res = requests.get(f"{base_url}/appointment_history/", timeout=60)
        return res.json() if res.status_code == 200 else []

    history_data = safe_api_call(fetch_history) or []
    total_appts = len(history_data)
    # Calculate appointment status from the database fields
    confirmed_count = len([a for a in history_data if not a.get("cancelled", False)])
    cancelled_count = len([a for a in history_data if a.get("cancelled", False)])

    # Your current database model does not have a "pending" field.
    pending_count = 0
    upcoming_count = confirmed_count + pending_count

    # 4 KPI Cards
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">Total Appointments</div>
        <div class="kpi-value">{total_appts}</div>
        <div class="kpi-description">
            All appointments
        </div>
    </div>
    """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
    <div class="kpi-card kpi-card-green">
        <div class="kpi-title">Confirmed</div>
        <div class="kpi-value">{confirmed_count}</div>
        <div class="kpi-description">
            Active appointments
        </div>
    </div>
    """, unsafe_allow_html=True)

    with col3:
       st.markdown(f"""
    <div class="kpi-card kpi-card-teal">
        <div class="kpi-title">Upcoming</div>
        <div class="kpi-value">{upcoming_count}</div>
        <div class="kpi-description">
            Scheduled appointments
        </div>
    </div>
    """, unsafe_allow_html=True)

    with col4:
        st.markdown(f"""
    <div class="kpi-card kpi-card-red">
        <div class="kpi-title">Cancelled</div>
        <div class="kpi-value">{cancelled_count}</div>
        <div class="kpi-description">
            Cancelled appointments
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Upcoming Appointments Table & Quick Actions Section
    tab_col, act_col = st.columns([2, 1])

    with tab_col:
        st.markdown("""
            <div class="dashboard-card">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
                    <h3 style="margin: 0; font-size: 17px;"><i class="bi bi-calendar-check" style="color: #1677FF;"></i> Upcoming Appointments</h3>
                    <span style="color: #1677FF; font-size: 13px; font-weight: 600;">View All</span>
                </div>
        """, unsafe_allow_html=True)

        if history_data:
            dashboard_rows = []

            for idx, item in enumerate(history_data[:5]):
                status_val = ("Cancelled" if item.get("cancelled", False) else "Confirmed")

                appointment_id = item.get("Appointment_id",idx + 1)
  
                start_time = str(item.get("start_time", ""))

                dashboard_rows.append({"ID": f"APT-{appointment_id:03d}",
                        "Patient": item.get("patient_name","N/A"),
                        "Reason": item.get("reason","Consultation"),
                        "Date": (start_time[:10] if len(start_time) >= 10 else "N/A"),
                        "Time": (start_time[11:16] if len(start_time) >= 16 else "N/A"),
                        "Status": status_val
                })
            df_display = pd.DataFrame(dashboard_rows)
            st.dataframe(df_display, use_container_width=True, hide_index=True)
        else:
            st.info("No appointment records available.")
        st.markdown("</div>", unsafe_allow_html=True)

    with act_col:
        st.markdown("""
            <div class="dashboard-card">
                <h3 style="margin-top: 0; font-size: 17px;"><i class="bi bi-telephone" style="color: #1677FF;"></i> AI Voice Assistant</h3>
                <p style="color: #64748B; font-size: 13px;">Need help with your appointment? Let our AI assistant handle it for you instantly.</p>
                <hr style="border: none; border-top: 1px solid #E2E8F0; margin: 12px 0;">
                <p style="font-weight: 600; font-size: 13px; color: #102A43;">Voice Agent Status:</p>
                <div style="background: #F0FDF4; padding: 8px 12px; border-radius: 6px; border: 1px solid #BBF7D0; margin-bottom: 12px;">
                    <span style="color: #16A34A; font-weight: 600; font-size: 13px;"><i class="bi bi-circle-fill" style="font-size: 8px;"></i> AI Assistant Online</span>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        dash_phone = st.text_input("Patient Phone Number", placeholder="+919876543210", key="dash_phone_input", label_visibility="collapsed")
        if st.button("Call AI Assistant", use_container_width=True):
            if not dash_phone:
                st.warning("Please enter a phone number.")
            else:
                def call_vapi():
                    return requests.post(f"{base_url}/call_shifa/", json={"phone_number": dash_phone}, timeout=10)
                res = safe_api_call(call_vapi)
                if res and res.status_code == 200:
                    st.success("Automated voice call initiated successfully!")

    st.markdown("<br>", unsafe_allow_html=True)

    # 4 Quick Action Cards
    qa1, qa2, qa3, qa4 = st.columns(4)
    with qa1:
        st.markdown("""
            <div class="dashboard-card" style="background: #F0F9FF; border-color: #BAE6FD;">
                <h4><i class="bi bi-calendar-plus" style="color: #1677FF;"></i> Book</h4>
                <p style="color: #64748B; font-size: 13px; margin-bottom: 0;">Schedule new patient consultations seamlessly.</p>
            </div>
        """, unsafe_allow_html=True)
    with qa2:
        st.markdown("""
            <div class="dashboard-card" style="background: #F0FDFA; border-color: #99F6E4;">
                <h4><i class="bi bi-arrow-repeat" style="color: #0F9D9A;"></i> Reschedule</h4>
                <p style="color: #64748B; font-size: 13px; margin-bottom: 0;">Modify appointment time slots effortlessly.</p>
            </div>
        """, unsafe_allow_html=True)
    with qa3:
        st.markdown("""
            <div class="dashboard-card" style="background: #FEF2F2; border-color: #FECACA;">
                <h4><i class="bi bi-calendar-x" style="color: #DC3545;"></i> Cancel</h4>
                <p style="color: #64748B; font-size: 13px; margin-bottom: 0;">Safely process appointment cancellations.</p>
            </div>
        """, unsafe_allow_html=True)
    with qa4:
        st.markdown("""
            <div class="dashboard-card" style="background: #FEFCE8; border-color: #FEF08A;">
                <h4><i class="bi bi-search" style="color: #F59E0B;"></i> Availability</h4>
                <p style="color: #64748B; font-size: 13px; margin-bottom: 0;">Check doctor availability in real-time.</p>
            </div>
        """, unsafe_allow_html=True)

# ==========================================
# 2. BOOK APPOINTMENT
# ==========================================
elif selected_menu == "Book Appointment":
    # st.header("Book Appointment")
    # st.caption("Fill in patient and scheduling details to book a consultation slot.")
    

    st.html("""
<div class="book-card">

    <div class="book-icon">
        <i class="bi bi-calendar-plus-fill"></i>
    </div>

    <div class="book-title">
        Book New Appointment
    </div>

    <div class="book-description">
        Schedule a hospital appointment by providing
        the patient's details, reason for consultation,
        and preferred date and time.
    </div>

    <div class="book-info">
        <i class="bi bi-shield-check"></i>
        Your appointment information is securely managed.
    </div>

</div>
""")

    st.markdown("---")

    with st.form("booking_form"):
        st.subheader("Patient Information")
        patient_name = st.text_input("Patient Name")
        reason = st.text_input("Reason for Visit")

        st.subheader("Appointment Information")
        col1, col2 = st.columns(2)
        with col1:
            appointment_date = st.date_input("Appointment Date", value=dt.date.today())
        with col2:
            appointment_time = st.time_input("Appointment Time", value=dt.time(9, 0))

        submitted = st.form_submit_button("Confirm Appointment")

        if submitted:
            if not patient_name or not reason:
                st.warning("Please provide both Patient Name and Reason for Visit.")
            else:
                start_datetime = dt.datetime.combine(appointment_date, appointment_time)
                payload = {
                    "patient_name": patient_name,
                    "reason": reason,
                    "start_time": start_datetime.isoformat()
                }

                def call_book():
                    return requests.post(f"{base_url}/book_appointments/", json=payload, timeout=60)

                response = safe_api_call(call_book)
                if response and response.status_code == 200:
                    st.success("Appointment successfully booked and saved to PostgreSQL.")
                    st.json(response.json())
                elif response:
                    st.error(response.text)

# ==========================================
# 3. MY APPOINTMENTS
# ==========================================
elif selected_menu == "My Appointments":
    st.html("""
<div class="my-appointments-card">

    <div class="my-appointments-icon">
        <i class="bi bi-calendar-check-fill"></i>
    </div>

    <div class="my-appointments-title">
        My Appointments
    </div>

    <div class="my-appointments-description">
        View and manage your scheduled hospital appointments.
        Check appointment details, dates, timings, and current
        appointment status in one place.
    </div>

    <div class="my-appointments-info">
        <i class="bi bi-info-circle-fill"></i>
        Your upcoming appointments are shown below.
    </div>

</div>
""")
    # st.header("My Appointments")
    # st.caption("Retrieve and review scheduled appointments for any selected date.")
    st.markdown("---")

    search_date = st.date_input("Select Date", value=dt.date.today())

    if st.button("Load Appointments"):
        payload = {"date": str(search_date)}

        def call_list():
            return requests.post(f"{base_url}/list_appointments/", json=payload, timeout=60)

        response = safe_api_call(call_list)
        if response and response.status_code == 200:
            appointments = response.json().get("appointments", [])
            if not appointments:
                st.info("No appointments found for this date.")
            else:
                st.dataframe(appointments, use_container_width=True)
        elif response:
            st.error(response.text)

# ==========================================
# 4. RESCHEDULE APPOINTMENT
# ==========================================
elif selected_menu == "Reschedule Appointment":
    st.html("""
<div class="reschedule-card">

    <div class="reschedule-icon">
        <i class="bi bi-calendar2-week"></i>
    </div>

    <div class="reschedule-title">
        Reschedule Appointment
    </div>

    <div class="reschedule-description">
        Change the date or time of an existing appointment.
        Please select a suitable available time before confirming
        the new appointment schedule.
    </div>

</div>
""")
    # st.header("Reschedule Appointment")
    # st.caption("Update schedule parameters for an active appointment identifier.")
    st.markdown("---")

    with st.form("reschedule_form"):
        appointment_id = st.number_input("Appointment ID", min_value=1, step=1)

        col1, col2 = st.columns(2)
        with col1:
            new_date = st.date_input("New Date", key="resch_date")
        with col2:
            new_time = st.time_input("New Time", key="resch_time")

        reschedule_submitted = st.form_submit_button("Reschedule Appointment")

        if reschedule_submitted:
            payload = {
                "appointment_id": int(appointment_id),
                "start_time": dt.datetime.combine(new_date, new_time).isoformat()
            }

            def call_resched():
                return requests.post(f"{base_url}/reschedule_appointments/", json=payload, timeout=60)

            response = safe_api_call(call_resched)
            if response and response.status_code == 200:
                st.success("Appointment successfully rescheduled.")
                st.json(response.json())
            elif response:
                st.error(response.text)

# ==========================================
# 5. CANCEL APPOINTMENT
# ==========================================
elif selected_menu == "Cancel Appointment":
    st.html("""
    <div class="cancel-card">

        <div class="cancel-icon">
            <i class="bi bi-calendar-x"></i>
        </div>

        <div class="cancel-title">
            Cancel Appointment
        </div>

        <div class="cancel-description">
            Please verify the appointment details before
            cancelling. Cancelled appointments cannot be
            restored automatically.
        </div>

    </div>
    """)
    # st.header("Cancel Appointment")
    # st.caption("Securely cancel an appointment using verification details.")
    st.markdown("---")

    with st.form("cancel_form"):
        cancel_id = st.number_input("Appointment ID", min_value=1, step=1, key="cancel_id")
        cancel_name = st.text_input("Patient Name for Verification", key="cancel_name")

        st.warning("Are you sure you want to cancel this appointment? This action is logged.")
        cancel_submitted = st.form_submit_button("Cancel Appointment")

        if cancel_submitted:
            if not cancel_name:
                st.warning("Please provide the patient name for verification.")
            else:
                payload = {
                    "appointment_id": int(cancel_id),
                    "patient_name": cancel_name,
                }

                def call_cancel():
                    return requests.post(f"{base_url}/cancel_appointments/", json=payload, timeout=60)

                response = safe_api_call(call_cancel)
                if response and response.status_code == 200:
                    st.success("Appointment successfully cancelled.")
                    st.json(response.json())
                elif response:
                    st.error(response.text)

# ==========================================
# 6. CHECK AVAILABILITY
# ==========================================
elif selected_menu == "Check Availability":
    st.html("""
<div class="availability-card">

    <div class="availability-icon">
        <i class="bi bi-calendar-check"></i>
    </div>

    <div class="availability-title">
        Check Appointment Availability
    </div>

    <div class="availability-description">
        Check available appointment slots before booking.
        Select your preferred date and time to find suitable
        available slots.
    </div>

</div>
""")
    # st.header("Check Availability")
    # st.caption("Verify if a specific date and time slot is open for booking.")
    st.markdown("---")

    col1, col2 = st.columns(2)
    with col1:
        check_date = st.date_input("Date", value=dt.date.today(), key="check_date")
    with col2:
        check_time = st.time_input("Time", value=dt.time(9, 0), key="check_time")

    if st.button("Check Availability"):
        payload = {
            "date": str(check_date),
            "start_time": str(check_time)
        }

        def call_avail():
            return requests.post(f"{base_url}/check_availability/", json=payload, timeout=60)

        response = safe_api_call(call_avail)
        if response and response.status_code == 200:
            available = response.json().get("available", False)
            if available:
                st.success("Slot is Available for booking.")
            else:
                st.error("Slot is NOT Available. Please choose another time.")
        elif response:
            st.error(response.text)

# ==========================================
# 7. AI VOICE ASSISTANT
# ==========================================
elif selected_menu == "AI Voice Assistant":
    st.html("""
<div class="voice-card">

    <div class="voice-icon">
        <i class="bi bi-telephone-forward-fill"></i>
    </div>

    <div class="voice-title">
        AI Voice Assistant
    </div>

    <div class="voice-description">
        Talk to our AI-powered hospital assistant to manage
        appointments, check availability, reschedule visits,
        and get assistance through a simple phone call.
    </div>

    <div class="voice-status">
        <span class="voice-status-dot"></span>
        AI Assistant Ready
    </div>

</div>
""")
    # st.header("AI Voice Assistant")
    # st.caption("Connect instantly with our conversational voice agent powered by Vapi AI.")
    st.markdown("---")

    st.info("Enter your mobile number below to receive an automated voice call from Shifa AI to manage your bookings interactively via voice commands.")

    with st.container():
        phone_number = st.text_input("Patient Phone Number", placeholder="+919876543210")

        if st.button("Call AI Assistant"):
            if not phone_number:
                st.warning("Please enter a valid phone number.")
            else:
                payload = {"phone_number": phone_number}

                def call_shifa():
                    return requests.post(f"{base_url}/call_shifa/", json=payload, timeout=60)

                response = safe_api_call(call_shifa)
                if response and response.status_code == 200:
                    st.success("Automated voice call initiated successfully! Your phone will ring shortly.")
                elif response:
                    st.error(response.text)

# ==========================================
# 8. APPOINTMENT HISTORY
# ==========================================
elif selected_menu == "Appointment History":

    st.html("""
<div class="history-card">

    <div class="history-icon">
        <i class="bi bi-clock-history"></i>
    </div>

    <div class="history-title">
        Appointment History
    </div>

    <div class="history-description">
        View the complete record of hospital appointments,
        including confirmed and cancelled appointments.
        Use the history to track previous and upcoming records.
    </div>

</div>
""")
    # st.header("Appointment History")
    # st.caption(
    #     "Complete historical record of all hospital appointments."
    # )
    st.markdown("---")

    # Fetch appointment history
    def fetch_full_history():
        response = requests.get(
            f"{base_url}/appointment_history/",
            timeout=30
        )

        if response.status_code == 200:
            return response.json()

        st.error(
            f"Unable to load appointment history. "
            f"Backend returned: {response.status_code}"
        )
        return []

    all_history = safe_api_call(fetch_full_history) or []

    # ------------------------------------------
    # Create clean appointment table
    # ------------------------------------------
    if all_history:

        # Status filter
        filter_status = st.selectbox(
            "Filter Status",
            ["All", "Confirmed", "Cancelled"]
        )

        table_rows = []

        for index, item in enumerate(all_history):

            # Determine status from database field
            if item.get("cancelled", False):
                status = "Cancelled"
            else:
                status = "Confirmed"

            # Apply filter
            if filter_status != "All" and status != filter_status:
                continue

            # Appointment ID
            appointment_id = item.get(
                "Appointment_id",
                index + 1
            )

            # Start time
            start_time = str(
                item.get("start_time", "")
            )

            # Extract date
            appointment_date = (
                start_time[:10]
                if len(start_time) >= 10
                else "N/A"
            )

            # Extract time
            appointment_time = (
                start_time[11:16]
                if len(start_time) >= 16
                else "N/A"
            )

            # Create table row
            table_rows.append({
                "Appointment ID": f"APT-{appointment_id:03d}",
                "Patient Name": item.get(
                    "patient_name",
                    "N/A"
                ),
                "Reason": item.get(
                    "reason",
                    "Consultation"
                ),
                "Date": appointment_date,
                "Time": appointment_time,
                "Status": status
            })

        # ------------------------------------------
        # Display table
        # ------------------------------------------
        if table_rows:

            history_df = pd.DataFrame(table_rows)

            st.dataframe(
                history_df,
                use_container_width=True,
                hide_index=True,
                column_config={
                    "Appointment ID": st.column_config.TextColumn(
                        "Appointment ID"
                    ),
                    "Patient Name": st.column_config.TextColumn(
                        "Patient Name"
                    ),
                    "Reason": st.column_config.TextColumn(
                        "Reason"
                    ),
                   "Date": st.column_config.TextColumn(
                        "Date"
                    ),
                    "Time": st.column_config.TextColumn(
                        "Time"
                    ),
                    "Status": st.column_config.TextColumn(
                        "Status"
                    )
                }
            )

            # Number of records
            st.caption(
                f"Showing {len(table_rows)} appointment(s)"
            )

        else:
            st.info(
                f"No {filter_status.lower()} appointments found."
            )

    else:
        st.info(
            "No appointment history records found "
            "in the PostgreSQL database."
        )

# ==========================================
# 9. ABOUT SYSTEM & ARCHITECTURE
# ==========================================
elif selected_menu == "About System":
    st.html("""
<div class="about-card">

    <div class="about-icon">
        <i class="bi bi-hospital-fill"></i>
    </div>

    <div class="about-title">
        About AI-Based Hospital Appointment System
    </div>

    <div class="about-description">
        An AI-powered hospital appointment management system
        designed to make booking, managing, and tracking
        hospital appointments simple, fast, and convenient.
    </div>

    <div class="about-info">
        <i class="bi bi-cpu-fill"></i>
        Powered by AI, FastAPI, PostgreSQL and Streamlit
    </div>

</div>
""")
    st.markdown("---")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Project Overview")
        st.write(
            "An AI-powered hospital appointment management system that combines Streamlit, FastAPI, "
            "PostgreSQL, SQLAlchemy, and Vapi AI to simplify appointment booking and voice-based patient interaction."
        )
    with col2:
        st.subheader("Technology Stack")
        st.markdown("""
        * **Frontend:** Python, Streamlit, Custom CSS
        * **Backend:** FastAPI, Python
        * **Database:** PostgreSQL, SQLAlchemy ORM
        * **Voice AI:** Vapi AI (Shifa Assistant)
        * **UI Framework:** Bootstrap Icons
        """)

    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader("System Architecture Workflow")
    
    st.markdown("""
        <div style="background: #FFFFFF; padding: 20px; border-radius: 12px; border: 1px solid #E2E8F0; text-align: center;">
            <p style="font-weight: 600; color: #0B2A4A; margin-bottom: 15px;">Application Request Flow</p>
            <div style="display: flex; justify-content: center; align-items: center; gap: 10px; flex-wrap: wrap; font-size: 13px;">
                <span style="background: #EAF4FF; padding: 8px 14px; border-radius: 6px; border: 1px solid #BAE6FD; font-weight: 600; color: #1677FF;">Patient Interface</span>
                <i class="bi bi-arrow-right" style="color: #64748B;"></i>
                <span style="background: #EAF4FF; padding: 8px 14px; border-radius: 6px; border: 1px solid #BAE6FD; font-weight: 600; color: #1677FF;">Streamlit Frontend</span>
                <i class="bi bi-arrow-right" style="color: #64748B;"></i>
                <span style="background: #EAF4FF; padding: 8px 14px; border-radius: 6px; border: 1px solid #BAE6FD; font-weight: 600; color: #1677FF;">FastAPI Backend</span>
                <i class="bi bi-arrow-right" style="color: #64748B;"></i>
                <span style="background: #EAF4FF; padding: 8px 14px; border-radius: 6px; border: 1px solid #BAE6FD; font-weight: 600; color: #1677FF;">PostgreSQL Database</span>
            </div>
            <hr style="border: none; border-top: 1px solid #E2E8F0; margin: 20px 0;">
            <p style="font-weight: 600; color: #0B2A4A; margin-bottom: 15px;">Voice AI Call Flow</p>
            <div style="display: flex; justify-content: center; align-items: center; gap: 10px; flex-wrap: wrap; font-size: 13px;">
                <span style="background: #F0FDFA; padding: 8px 14px; border-radius: 6px; border: 1px solid #99F6E4; font-weight: 600; color: #0F9D9A;">Patient Phone</span>
                <i class="bi bi-arrow-left-right" style="color: #64748B;"></i>
                <span style="background: #F0FDFA; padding: 8px 14px; border-radius: 6px; border: 1px solid #99F6E4; font-weight: 600; color: #0F9D9A;">Vapi AI Voice Agent</span>
                <i class="bi bi-arrow-left-right" style="color: #64748B;"></i>
                <span style="background: #F0FDFA; padding: 8px 14px; border-radius: 6px; border: 1px solid #99F6E4; font-weight: 600; color: #0F9D9A;">FastAPI Webhook</span>
                <i class="bi bi-arrow-left-right" style="color: #64748B;"></i>
                <span style="background: #F0FDFA; padding: 8px 14px; border-radius: 6px; border: 1px solid #99F6E4; font-weight: 600; color: #0F9D9A;">PostgreSQL</span>
            </div>
        </div>
    """, unsafe_allow_html=True)
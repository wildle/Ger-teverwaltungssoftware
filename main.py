### Erste Streamlit App
import time
import streamlit as st
import pandas as pd
from queries import find_devices
from devices import Device
from datetime import datetime, timedelta
from tab2_Nutzerverwaltung import user_management
from tab1_Geraeteverwaltung import device_management
from tab4_Wartungsmanagement import wartungsmanagement
from tab3_Reservierungssystem import reservation_system
from users import User  # Stellen Sie sicher, dass Sie den User importiert haben

# Create a new session_state if it doesn't exist
if 'user' not in st.session_state:
    st.session_state.user = User('Test User', 'testuser@example.com', 'test role')

# Use the user from session_state instead of creating a new one
user = st.session_state.user

# Eine Überschrift der ersten Ebene
st.write("# Gerätemanagement")

tab1, tab2, tab3, tab4 = st.tabs(["Geräte-Verwaltung", "Nutzer-Verwaltung", "Reservierungssystem", "Wartungs-Management"])

device_management(tab1)
# Aufruf der der Nutzer-Verwaltung
user_management(tab2)
reservation_system(tab3)
wartungsmanagement(tab4)

# Eine Auswahlbox mit Datenbankabfrage, das Ergebnis wird in current_device gespeichert
devices_in_db = find_devices()

if devices_in_db:
    current_device_name = st.selectbox(
        'Gerät auswählen',
        options = devices_in_db, key="sbDevice")

    if current_device_name in devices_in_db:
        loaded_device = Device.load_data_by_device_name(current_device_name)
        st.write(f"Loaded Device: {loaded_device}")

    with st.form("Device"):
        st.write(loaded_device.device_name)

        #checkbox_val = st.checkbox("Is active?", value=loaded_device.is_active)
        #loaded_device.is_active = checkbox_val

        text_input_val = st.text_input("Geräte-Verantwortlicher", value=loaded_device.managed_by_user_id)
        loaded_device.managed_by_user_id = text_input_val

        # Every form must have a submit button.
        submitted = st.form_submit_button("Submit")
        if submitted:
            loaded_device.store_data()
            st.write("Data stored.")
            st.rerun()
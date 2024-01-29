import streamlit as st
from queries import QueryDB
from devices import Device
from device_management import display_device_management
from user_management import display_user_management
from reservation_management import display_reservation_system
from maintenance_management import display_maintenance_management

# Create a sidebar
sidebar = st.sidebar

# Create tabs in the sidebar
tab = sidebar.radio("Go to", ["Geräteverwaltung", "Nutzerverwaltung", "Reservierungssystem", "Wartungsmanagement"])

# Depending on the selected tab, display the corresponding content
if tab == "Geräteverwaltung":
    display_device_management()
elif tab == "Nutzerverwaltung":
    display_user_management()
elif tab == "Reservierungssystem":
    display_reservation_system()
elif tab == "Wartungsmanagement":
    display_maintenance_management()
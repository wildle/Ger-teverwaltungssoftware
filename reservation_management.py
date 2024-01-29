import streamlit as st
from devices import Device
from users import User
from reservations import Reservation

def display_reservation_management():
    st.title("Reservierungssystem")

    # Formular zum Anlegen einer neuen Reservierung
    with st.form(key='reservation_form'):
        st.subheader("Neue Reservierung anlegen")
        device_name = st.selectbox('Gerät auswählen', options=Device.get_all_device_names())
        user_email = st.selectbox('Nutzer auswählen', options=User.get_all_user_emails())
        reservation_start = st.date_input('Reservierungsbeginn')
        reservation_end = st.date_input('Reservierungsende')
        submit_button = st.form_submit_button(label='Reservierung anlegen')

    # Wenn das Formular abgeschickt wird, erstelle eine neue Reservierung und speichere sie in der Datenbank
    if submit_button:
        new_reservation = Reservation(device_name=device_name, user_email=user_email, start_date=reservation_start, end_date=reservation_end)
        if new_reservation.is_valid():
            new_reservation.store_data()
            st.success(f"Reservierung für {device_name} wurde erfolgreich angelegt.")
        else:
            st.error("Die Reservierung ist ungültig. Bitte überprüfen Sie die Daten und versuchen Sie es erneut.")
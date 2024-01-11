### Erste Streamlit App

import streamlit as st
import pandas as pd
from queries import find_devices
from devices import Device
from datetime import datetime, timedelta


class Device:
    def __init__(self, device_name, last_maintenance_date):
        self.device_name = device_name
        self.last_maintenance_date = last_maintenance_date


# Eine Überschrift der ersten Ebene
st.write("# Gerätemanagement")

tab1, tab2, tab3, tab4 = st.tabs(["Geräte-Verwaltung", "Nutzer-Verwaltung", "Reservierungssystem", "Wartungs-Management"])
with tab1:
    st.header("Geräte-Verwaltung")

    if st.button("Gerät anlegen"):
        with st.form("Gerät anlegen"):

            device_id = st.text_input("Geräte-ID")
            device_name = st.text_input("Gerätename")
            user = st.text_input("Nutzer")
            last_update = st.text_input("Letzte Änderung des Geräts")
            creation_date = st.text_input("Erstellungsdatum des Geräts")
            end_of_life = st.text_input("Datum, ab welchem das Gerät nicht mehr gewartet wird")

            submitted = st.form_submit_button("Speichern")
            if submitted:
                # Schritt 5: System speichert Gerätedaten
                st.write(f"Gerät angelegt mit folgenden Daten:")
                st.write(f"ID: {device_id}")
                st.write(f"Gerätename: {device_name}")
                st.write(f"Nutzer: {user}")
                st.write(f"Letztes Update: {last_update}")
                st.write(f"Erstellungsdatum: {creation_date}")
                st.write(f"Enddatum: {end_of_life}")
                st.success("Gerät erfolgreich gespeichert!")

    if st.button("Gerät ändern"):
        with st.form("Gerät ändern"):
            st.write("Gerät auswählen")

            current_device_example = st.selectbox(
            'Gerät auswählen',
            options = ["Gerät_A", "Gerät_B"], key="sbDevice")
            submitted = st.form_submit_button("auswählen")

with tab2:
    st.header("Nutzer Verwaltung")
    
    if st.button("Nutzer anlegen"):
            
        with st.form("Neuer Nutzer"):
            user_name = st.text_input("Nutzername")
            user_email = st.text_input("E-Mail-Adresse")
            user_role = st.selectbox("Rolle", ["Geräteverantwortlicher", "Reservierer"])

            submitted = st.form_submit_button("bestätigen")
            if submitted:
                st.write(f"Nutzer angelegt mit folgenden Daten:")
                st.write(f"Nutzername: {user_name}")
                st.write(f"E-Mail: {user_email}")
                st.write(f"Rolle: {user_role}")
                st.success("Nutzer erfolgreich angelegt!")


with tab3:
    st.write("## Geräteauswahl")

    # Eine Auswahlbox mit hard-gecoded Optionen, das Ergebnis wird in current_device_example gespeichert
    current_device_example = st.selectbox('Gerät auswählen',options = ["Gerät_A", "Gerät_B"], key="sbDevice_example")
    st.header("Reservierungssystem")

    reservation_period =  st.text_input("Zeitraum")
    reservation_reason = st.text_area("Grund")
    
    if st.button("Speichern"):
        # Schritt 5: System speichert Reservierungsdaten
        st.write(f"Reservierung angelegt/geändert mit folgenden Daten:")
        st.write(f"Zeitraum: {reservation_period}")
        st.write(f"Grund: {reservation_reason}")
        st.success("Gerät erfolgreich gespeichert!")


with tab4:
    st.header("Wartungs-Management")

    devices = [
        Device("Gerät A", None),
        Device("Gerät B", None),
    ]

    data = []
    for device in devices:
        if device.last_maintenance_date:
            next_maintenance_date = device.last_maintenance_date + timedelta(days=90)
            data.append([device.device_name, next_maintenance_date.strftime('%Y-%m-%d')])
        else:
            data.append([device.device_name, None])

    df = pd.DataFrame(data, columns=['Gerät', 'Nächster Wartungstermin'])
    st.table(df)

    st.header("Wartungskosten pro Quartal")

    daten = {'Quartal 1': [0],
         'Quartal 2': [0],
         'Quartal 3': [0],
         'Quartal 4': [0]}

    output_df = pd.DataFrame(daten)

    st.table(output_df)


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
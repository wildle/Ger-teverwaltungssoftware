import streamlit as st
from devices import Device 

def device_management(tab):
    with tab:
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
                    # Create an instance of the Device class and store the data
                    new_device = Device(device_name=device_name, managed_by_user_id=user)
                    new_device.store_data()

                    st.success("Gerät erfolgreich gespeichert!")

        if st.button("Gerät ändern"):
            with st.form("Gerät ändern"):
                st.write("Gerät auswählen")

                # Load existing devices from the database
                existing_devices = Device.db_connector.all()

                current_device_example = st.selectbox(
                    'Gerät auswählen',
                    options=[device['device_name'] for device in existing_devices], key="sbDevice")

                submitted = st.form_submit_button("auswählen")

                if submitted:
                    st.write(f"Ausgewähltes Gerät: {current_device_example}")

                    # You can load the selected device's data and display it
                    selected_device = Device.load_data_by_device_name(current_device_example)

                    if selected_device:
                        st.write("Daten des ausgewählten Geräts:")
                        st.write(f"Gerätename: {selected_device.device_name}")
                        st.write(f"Managed by User ID: {selected_device.managed_by_user_id}")
                        st.write(f"Status: {'Aktiv' if selected_device.is_active else 'Inaktiv'}")
                    else:
                        st.warning("Gerät nicht gefunden.")
import streamlit as st
from queries import QueryDB
from devices import Device

def display_device_management():
    # Eine Überschrift der ersten Ebene
    st.write("# Gerätemanagement")

    # Eine Überschrift der zweiten Ebene
    st.write("## Geräteauswahl")

    # Eine Auswahlbox mit Datenbankabfrage, das Ergebnis wird in current_device gespeichert
    devices_in_db = QueryDB.find_devices()

    if devices_in_db:
        current_device_name = st.selectbox(
            'Gerät auswählen',
            options=devices_in_db, key="sbDevice")

        if current_device_name in devices_in_db:
            loaded_device = Device.load_data_by_device_name(current_device_name)
            st.write(f"Loaded Device: {loaded_device}")

            with st.form("Device"):
                st.write(loaded_device.device_name)

                text_input_val = st.text_input("Geräte-Verantwortlicher", value=loaded_device.managed_by_user_id)
                loaded_device.managed_by_user_id = text_input_val

                # Every form must have a submit button.
                submitted = st.form_submit_button("Submit")
                if submitted:
                    loaded_device.store_data()
                    st.write("Data stored.")
                    st.rerun()

            # Button to delete the current device
            if st.button('Delete Device'):
                Device.delete_device(current_device_name)
                st.write(f"Device {current_device_name} deleted.")
                st.rerun()

    # Form to add a new device
    with st.form("New Device"):
        new_device_name = st.text_input("Device Name")
        new_managed_by_user_id = st.text_input("Managed By User ID")
        new_end_of_life = st.text_input("End of Life")
        new_quarterly_costs = st.text_input("Kosten pro Quartal")

        # Every form must have a submit button.
        submitted = st.form_submit_button("Add Device")
        if submitted:
            new_device = Device(new_device_name, new_managed_by_user_id, new_end_of_life)
            new_device.quarterly_costs = new_quarterly_costs
            QueryDB.insert_device(new_device.__dict__)
            st.write(f"Device {new_device_name} added.")
            st.rerun()

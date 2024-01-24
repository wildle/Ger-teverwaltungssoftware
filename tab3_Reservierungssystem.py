import streamlit as st
def reservation_system(tab):
    with tab:
        st.header("Reservierungssystem")

        if st.button("Reservierung anlegen/ändern"):
            with st.form("Reservierung anzeigen"):
                 # Eine Auswahlbox mit hard-gecoded Optionen, das Ergebnis wird in current_device_example gespeichert
                current_device_example = st.selectbox('Gerät auswählen',options = ["Neues_Gerät", "Gerät_A", "Gerät_B"], key="sbDevice_example")
                st.header("Reservierungssystem")

                reservation_period =  st.text_input("Zeitraum")
                reservation_reason = st.text_area("Grund")

                submitted = st.form_submit_button("Speichern")
                if submitted:
                    # Schritt 5: System speichert Reservierungsdaten
                    st.write(f"Reservierung angelegt/geändert mit folgenden Daten:")
                    st.write(f"Zeitraum: {reservation_period}")
                    st.write(f"Grund: {reservation_reason}")
                    st.success("Gerät erfolgreich gespeichert!")

        if st.button("Reservierung anzeigen"):
            with st.form("Reservierung anzeigen"):
                # Eine Auswahlbox mit hard-gecoded Optionen, das Ergebnis wird in current_device_example gespeichert
                current_device_example = st.selectbox('Gerät auswählen',options = ["Gerät_A", "Gerät_B"], key="sbDevice_example")
                submitted = st.form_submit_button("auswählen")


       
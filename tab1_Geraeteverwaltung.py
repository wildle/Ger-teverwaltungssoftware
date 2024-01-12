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

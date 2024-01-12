def reservation_system(tab):
    with tab:
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

# Verwendung der Funktion
reservation_system(tab3)
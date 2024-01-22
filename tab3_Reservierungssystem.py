import streamlit as st
def reservation_system():
    st.title("Reservierungssystem")
    reservation_system = ReservationSystem()

    tab = st.tabs(2, ["Reservierung anlegen/ändern", "Reservierung anzeigen"])

    if tab == "Reservierung anlegen/ändern":
        with st.form("Reservierung anlegen/ändern"):
            current_device = st.selectbox('Gerät auswählen', options=["Neues_Gerät", "Gerät_A", "Gerät_B"], key="sbDevice")
            reservation_period = st.text_input("Zeitraum")
            reservation_reason = st.text_area("Grund")
            submitted = st.form_submit_button("Speichern")

            if submitted:
                reservation_system.create_reservation(current_device, reservation_period, reservation_reason)
                st.success("Reservierung erfolgreich gespeichert!")

    elif tab == "Reservierung anzeigen":
        with st.form("Reservierung anzeigen"):
            selected_device = st.selectbox('Gerät auswählen', options=["Gerät_A", "Gerät_B"], key="sbDevice_show")
            submitted_show = st.form_submit_button("Anzeigen")

            if submitted_show:
                reservations = reservation_system.get_reservations(selected_device)
                if reservations:
                    st.header(f"Reservierungen für {selected_device}")
                    for reservation in reservations:
                        st.write(f"Zeitraum: {reservation['period']}")
                        st.write(f"Grund: {reservation['reason']}")
                        st.write("---")
                else:
                    st.warning("Keine Reservierungen für das ausgewählte Gerät gefunden.")

if __name__ == "__main__":
    main()




       
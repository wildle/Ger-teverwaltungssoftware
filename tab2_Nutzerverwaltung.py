def user_management(tab):
    with tab:
        st.header("Nutzer-Verwaltung")
        
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
import streamlit as st
from users import User

def display_user_management():
    st.title("Nutzerverwaltung")

    # Formular zum Anlegen eines neuen Nutzers
    with st.form(key='user_form'):
        st.subheader("Neuen Nutzer anlegen")
        username = st.text_input(label='Nutzername')
        email = st.text_input(label='E-Mail-Adresse')
        submit_button = st.form_submit_button(label='Nutzer anlegen')

    # Wenn das Formular abgeschickt wird, erstelle einen neuen Nutzer und speichere ihn in der Datenbank
    if submit_button:
        new_user = User(user_id=email, username=username, email=email)
        new_user.store_data()
        st.success(f"Nutzer {username} wurde erfolgreich angelegt.")
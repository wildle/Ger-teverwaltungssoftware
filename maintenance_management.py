import streamlit as st
from maintenance import Maintenance

def display_maintenance_management():
    st.title('Wartungs-Management')

    # Nächste Wartungstermine anzeigen
    next_maintenance_dates = Maintenance.get_next_maintenance_dates()
    st.subheader('Nächste Wartungstermine')
    for device_name, date in next_maintenance_dates.items():
        st.text(f'Gerät: {device_name}, Datum: {date}')

    # Wartungskosten pro Quartal anzeigen
    quarterly_maintenance_costs = Maintenance.get_quarterly_maintenance_costs()
    st.subheader('Wartungskosten pro Quartal')
    for quarter, cost in quarterly_maintenance_costs.items():
        st.text(f'Quartal: {quarter}, Kosten: {cost}')
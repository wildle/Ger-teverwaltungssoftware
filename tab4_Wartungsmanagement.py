import streamlit as st
def wartungsmanagement(tab):
    with tab:
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
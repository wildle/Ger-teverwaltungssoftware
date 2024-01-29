class Reservation:
    def __init__(self, device_name, user_email, start_date, end_date):
        self.device_name = device_name
        self.user_email = user_email
        self.start_date = start_date
        self.end_date = end_date

    def is_valid(self):
        # Überprüfen Sie, ob die Reservierung gültig ist
        # Hier sollten Sie den Code hinzufügen, der überprüft, ob das Gerät zur gewünschten Zeit verfügbar ist
        return True

    def store_data(self):
        # Speichern Sie die Reservierungsdaten
        # Hier sollten Sie den Code hinzufügen, der die Reservierungsdaten in der Datenbank speichert
        pass
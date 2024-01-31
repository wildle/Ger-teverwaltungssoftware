from tinydb import TinyDB, Query
from datetime import datetime
import os
from serializer import serializer

class Reservation:
    db_connector = TinyDB(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'database.json'), storage=serializer).table('reservations')

    def __init__(self, device_name, user_email, start_date, end_date):
        self.device_name = device_name
        self.user_email = user_email
        self.start_date = start_date
        self.end_date = end_date

    def store_data(self):
        print("Storing data...")
        DeviceQuery = Query()
        result = self.db_connector.search(DeviceQuery.device_name == self.device_name)
        if result:
            self.__last_update = datetime.now()
            result = self.db_connector.update(self.__dict__, doc_ids=[result[0].doc_id])
            print("Data updated.")
        else:
            self.db_connector.insert(self.__dict__)
            print("Data inserted.")

    @classmethod
    def load_data(cls, user_email):
        ReservationQuery = Query()
        return cls.table.search(ReservationQuery.user_email == user_email)

    @classmethod
    def delete_reservation(cls, user_email):
        ReservationQuery = Query()
        cls.table.remove(ReservationQuery.user_email == user_email)

    @classmethod
    def get_all_reservations(cls):
        return cls.db_connector.all()

    def __str__(self):
        return f'Reservation({self.device_name}, {self.user_email}, {self.start_date}, {self.end_date})'

    def __repr__(self):
        return self.__str__()

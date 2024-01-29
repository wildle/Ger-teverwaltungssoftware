import os
from datetime import datetime
from users import User
from tinydb import TinyDB, Query
from serializer import serializer

class Device():
    db_connector = TinyDB(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'database.json'), storage=serializer).table('devices')

    def __init__(self, device_name : str, managed_by_user_id : str, end_of_life : str):
        self.device_name = device_name
        self.managed_by_user_id = managed_by_user_id
        self.is_active = True
        self.end_of_life = end_of_life
        self.__creation_date = datetime.now()
        self.__last_update = datetime.now()

    def __str__(self):
        return f'Device {self.device_name} ({self.managed_by_user_id})'

    def __repr__(self):
        return self.__str__()

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
    def load_data_by_device_name(cls, device_name):
        DeviceQuery = Query()
        result = cls.db_connector.search(DeviceQuery.device_name == device_name)

        if result:
            data = result[0]
            return cls(data['device_name'], data['managed_by_user_id'], data['end_of_life'])
        else:
            return None

    @classmethod
    def delete_device(cls, device_name):
        DeviceQuery = Query()
        cls.db_connector.remove(DeviceQuery.device_name == device_name)
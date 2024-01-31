import os
from datetime import datetime
from tinydb import TinyDB, Query
from serializer import serializer

class Device:
    db_connector = TinyDB(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'database.json'), storage=serializer).table('devices')

    def __init__(self, device_name: str, managed_by_user_id: str, end_of_life: str, quarterly_costs: float = 0.0):
        self.device_name = device_name
        self.managed_by_user_id = managed_by_user_id
        self.is_active = True
        self.end_of_life = end_of_life
        self.quarterly_costs = quarterly_costs
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
            end_of_life = data['end_of_life'] if 'end_of_life' in data else None
            quarterly_costs = data['quarterly_costs'] if 'quarterly_costs' in data else 0.0
            return cls(data['device_name'], data['managed_by_user_id'], end_of_life, quarterly_costs)
        else:
            return None

    @classmethod
    def delete_device(cls, device_name):
        DeviceQuery = Query()
        cls.db_connector.remove(DeviceQuery.device_name == device_name)

    @classmethod
    def get_all_device_names(cls):
        DeviceQuery = Query()
        all_devices = cls.db_connector.search(DeviceQuery.device_name.exists())
        return [device['device_name'] for device in all_devices]

import os

from users import User

from tinydb import TinyDB, Query
from serializer import serializer


class Device():
    # Class variable that is shared between all instances of the class
    db_connector = TinyDB(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'database.json'), storage=serializer).table('devices')

    # Constructor
    def __init__(self, device_name : str, managed_by_user_id : str):
        self.device_name = device_name
        # The user id of the user that manages the device
        # We don't store the user object itself, but only the id (as a key)
        self.managed_by_user_id = managed_by_user_id
        self.is_active = True
        
    # String representation of the class
    def __str__(self):
        return f'Device {self.device_name} ({self.managed_by_user_id})'

    # String representation of the class
    def __repr__(self):
        return self.__str__()
    
    def store_data(self):
        print("Storing data...")
        # Check if the device already exists in the database
        DeviceQuery = Query()
        result = self.db_connector.search(DeviceQuery.device_name == self.device_name)
        if result:
            # Update the existing record with the current instance's data
            result = self.db_connector.update(self.__dict__, doc_ids=[result[0].doc_id])
            print("Data updated.")
        else:
            # If the device doesn't exist, insert a new record
            self.db_connector.insert(self.__dict__)
            print("Data inserted.")
            
    # Class method that can be called without an instance of the class to construct an instance of the class
    @classmethod
    def load_data_by_device_name(cls, device_name):
        # Load data from the database and create an instance of the Device class
        DeviceQuery = Query()
        result = cls.db_connector.search(DeviceQuery.device_name == device_name)

        if result:
            data = result[0]
            return cls(data['device_name'], data['managed_by_user_id'])
        else:
            return None



if __name__ == "__main__":
    # Create a device
    device1 = Device("Device1", "one@mci.edu")
    device2 = Device("Device2", "two@mci.edu") 
    device3 = Device("Device3", "two@mci.edu") 
    device1.store_data()
    device2.store_data()
    device3.store_data()
    device4 = Device("Device3", "four@mci.edu") 
    device4.store_data()

    loaded_device = Device.load_data_by_device_name('Device2')
    if loaded_device:
        print(f"Loaded Device: {loaded_device}")
    else:
        print("Device not found.")

    
import os
from tinydb import TinyDB, Query
from serializer import serializer

class QueryDB:
    db_connector = TinyDB(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'database.json'), storage=serializer)

    @classmethod
    def find_devices(cls) -> list:
        """Find all devices in the database."""
        devices_table = cls.db_connector.table('devices')
        DeviceQuery = Query()
        result = devices_table.all()

        if result:
            result = [x["device_name"] for x in result]

        return result

    @classmethod
    def find_users(cls) -> list:
        """Find all users in the database."""
        users_table = cls.db_connector.table('users')
        UserQuery = Query()
        result = users_table.all()

        if result:
            result = [x["username"] for x in result]

        return result

    @classmethod
    def insert_device(cls, device):
        """Insert a new device in the database."""
        devices_table = cls.db_connector.table('devices')
        devices_table.insert(device)

    @classmethod
    def search_device(cls, device_name):
        """Search for a device in the database."""
        devices_table = cls.db_connector.table('devices')
        DeviceQuery = Query()
        return devices_table.search(DeviceQuery.device_name == device_name)

    @classmethod
    def update_device(cls, device_name, new_data):
        """Update a device in the database."""
        devices_table = cls.db_connector.table('devices')
        DeviceQuery = Query()
        devices_table.update(new_data, DeviceQuery.device_name == device_name)

    @classmethod
    def remove_device(cls, device_name):
        """Remove a device from the database."""
        devices_table = cls.db_connector.table('devices')
        DeviceQuery = Query()
        devices_table.remove(DeviceQuery.device_name == device_name)

if __name__ == "__main__":
    print(QueryDB.find_devices())
    print(QueryDB.find_users())
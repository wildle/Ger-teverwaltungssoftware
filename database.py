from tinydb import TinyDB, Query

class Database:
    def __init__(self, db_path):
        self.db = TinyDB(db_path)
        print(f"Database initialized with path: {db_path}")

    def insert(self, table_name, data):
        table = self.db.table(table_name)
        table.insert(data)
        print(f"Inserted data into table {table_name}: {data}")

    def all(self, table_name):
        table = self.db.table(table_name)
        return table.all()

    def search(self, table_name, condition):
        table = self.db.table(table_name)
        return table.search(condition)

    def update(self, table_name, data, condition):
        table = self.db.table(table_name)
        table.update(data, condition)

    def remove(self, table_name, condition):
        table = self.db.table(table_name)
        table.remove(condition)

class Device:
    def __init__(self, device_name : str, managed_by_user_id : str, reservation, db_connector : Database):
        self.device_name = device_name
        self.managed_by_user_id = managed_by_user_id
        self.is_active = True
        self.reservation = reservation
        self.db_connector = db_connector

    def to_dict(self):
        return {
            'device_name': self.device_name,
            'managed_by_user_id': self.managed_by_user_id,
            'is_active': self.is_active,
            'reservation': self.reservation  # Make sure this is also serializable
        }

    def store_data(self):
        print("Storing data...")
        DeviceQuery = Query()
        result = self.db_connector.search('devices_with_subclass', DeviceQuery.device_name == self.device_name)

        if result:
            self.db_connector.update('devices_with_subclass', self.to_dict(), doc_ids=[result[0].doc_id])
            print("Data updated.")
        else:
            self.db_connector.insert('devices_with_subclass', self.to_dict())
            print("Data inserted.")

    @classmethod
    def load_data_by_device_name(cls, device_name, db_connector):
        DeviceQuery = Query()
        result = db_connector.search('devices_with_subclass', DeviceQuery.device_name == device_name)

        if result:
            data = result[0]
            return cls(data['device_name'], data['managed_by_user_id'], data['reservation'], db_connector)
        else:
            return None

if __name__ == "__main__":
    db = Database('database.json')
    device = Device('device1', 'user1', None, db)
    device.store_data()
    loaded_device = Device.load_data_by_device_name('device1', db)
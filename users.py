from tinydb import TinyDB, Query

class User:
    def __init__(self, id, name, role) -> None:
        self.id = id
        self.name = name
        self.role = role
        self.db = TinyDB('db.json')  # replace 'db.json' with the path to your database file

    def store_data(self):
        self.db.insert({'id': self.id, 'name': self.name, 'role': self.role})

    def update_data(self, name=None, role=None):
        User = Query()
        updated_data = {}
        if name is not None:
            updated_data['name'] = name
        if role is not None:
            updated_data['role'] = role
        self.db.update(updated_data, User.id == self.id)

    def delete_data(self):
        User = Query()
        self.db.remove(User.id == self.id)

    @staticmethod
    def load_data_by_user_id(id):
        User = Query()
        return db.search(User.id == id)
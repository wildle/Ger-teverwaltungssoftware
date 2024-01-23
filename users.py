from database import Database
from tinydb import TinyDB, Query
from uuid import uuid4

class User:
    def __init__(self, name, email, role):
        self.id = str(uuid4())  # Generate a unique ID
        self.name = name
        self.email = email
        self.role = role
        self.db = Database('database.json')

    def store_data(self):
        self.db.insert('users', {'id': self.id, 'name': self.name, 'email': self.email, 'role': self.role})

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

    def load_data_by_user_id(self, id):
        User = Query()
        return self.db.search(User.id == id)
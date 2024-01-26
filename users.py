from database import Database
from tinydb import TinyDB, Query
from uuid import uuid4

class User:

    db = Database(r'C:\Users\Lenard\Documents\Mechatronik, Design & Innovation Lokal\3. Semester_WS2324\Softwaredesign\Geraeteverwaltungssoftware\database.json')
    def __init__(self, name, email, role):
        self.id = str(uuid4())  # Generate a unique ID
        self.name = name
        self.email = email
        self.role = role
        

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

    @classmethod
    def load_data_by_user_name(cls, user_name):
        # Initialize the database
        db = cls.db

        # Load the data from the database
        data = db.all('users')

        # Find the user with the given name
        for user_data in data:
            if user_data['name'] == user_name:
                # Create a new User object and return it
                return cls(user_data['name'], user_data['email'], user_data['role'])

        # If no user with the given name was found, return None
        return None

if __name__ == "__main__":
    user = User('Test User', 'testuser@example.com', 'test role')
    user.store_data()
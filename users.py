from tinydb import TinyDB, Query
import os

class User:
    def __init__(self, id, name) -> None:
        self.id = id
        self.name = name
        self.db = TinyDB(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'database.json')).table('users')

    def store_data(self):
        # Check if user already exists
        UserQuery = Query()
        search_result = self.db.search(UserQuery.id == self.id)
        if search_result:
            # Update existing user
            self.db.update({'name': self.name}, UserQuery.id == self.id)
        else:
            # Insert new user
            self.db.insert({'id': self.id, 'name': self.name})

    @staticmethod
    def load_data_by_user_id(id):
        db = TinyDB(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'database.json')).table('users')
        UserQuery = Query()
        user_data = db.search(UserQuery.id == id)
        if user_data:
            return user_data[0]  # Return the first match
        else:
            return None  # Return None if no match found
from tinydb import TinyDB, Query

class User:
    db_connector = TinyDB('database.json')
    table = db_connector.table('users')

    def __init__(self, user_id, username, email):
        self.user_id = user_id
        self.username = username
        self.email = email

    def store_data(self):
        self.table.insert(self.__dict__)

    @classmethod
    def load_data(cls, user_id):
        User = Query()
        return cls.table.search(User.user_id == user_id)

    @classmethod
    def delete_user(cls, user_id):
        User = Query()
        cls.table.remove(User.user_id == user_id)

    @classmethod
    def update_user(cls, user_id, new_data):
        User = Query()
        cls.table.update(new_data, User.user_id == user_id)

    @classmethod
    def get_all_user_emails(cls):
        UserQuery = Query()
        all_users = cls.table.search(UserQuery.email.exists())
        return [user['email'] for user in all_users]

    def __str__(self):
        return f'User({self.user_id}, {self.username}, {self.email})'

    def __repr__(self):
        return self.__str__()
        
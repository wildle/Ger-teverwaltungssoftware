class User:
    def __init__(self, id, name) -> None:
        self.id = id
        self.name = name

    def store_data(self):
        # Implement this method to store user data in the database
        pass

    @staticmethod
    def load_data_by_user_id(id):
        # Implement this method to load user data from the database
        pass
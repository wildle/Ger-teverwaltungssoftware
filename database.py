from tinydb import TinyDB, Query

class Database:
    def __init__(self, db_path):
        self.db = TinyDB(db_path)

    def insert(self, table_name, data):
        table = self.db.table(table_name)
        table.insert(data)

    def search(self, table_name, condition):
        table = self.db.table(table_name)
        return table.search(condition)

    def update(self, table_name, data, condition):
        table = self.db.table(table_name)
        table.update(data, condition)

    def remove(self, table_name, condition):
        table = self.db.table(table_name)
        table.remove(condition)
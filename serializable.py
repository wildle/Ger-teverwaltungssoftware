from abc import ABC, abstractmethod
from database_inheritance import DatabaseConnector
from tinydb import TinyDB, Query

class Serializable(ABC):

    @abstractmethod
    def __init__(self, id):
        self.id = id
    
    @classmethod
    def find_all(cls):
        return cls.get_db_connector().all()

    @classmethod
    @abstractmethod
    def get_db_connector(cls):
        return None
    
    @classmethod
    @abstractmethod
    def load_by_id(cls, id):
        query = Query()
        result = cls.get_db_connector().search(query.id == id)
        if result:
            return result[0]
        else:
            return None

    def store(self) -> None:
        print("  Storing data...")
        query = Query()
        result = self.get_db_connector().search(query.id == self.id)

        if result:
            result = self.get_db_connector().update(self.to_dict(), doc_ids=[result[0].doc_id])
            print("  Data updated.")
        else:
            self.get_db_connector().insert(self.to_dict())
            print("  Data inserted.")

    def delete(self) -> None:
        query = Query()
        result = self.get_db_connector().remove(query.id == self.id)

    #Do not modify this function unless you really know what you are doing!
    def to_dict(self, obj=None):
        """
        This function converts an object recursively into a dict.
        It is not neccessary to understand how this function works!
        For the sake of simplicity it doesn't handle class attributes and callable objects like (callback) functions as attributes well
        """
        #If no object is passed to the function convert the object itself
        if obj is None:
            obj = self
            
        if isinstance(obj, dict):
            #If the object is a dict try converting all its values into dicts also
            data = {}
            for (k, v) in obj.items():
                data[k] = self.to_dict(v)
            return data
        elif hasattr(obj, "__iter__") and not isinstance(obj, str):
            #If the object is iterable (lists, etc.) try converting all its values into dicts
            #Strings are also iterable, but theses should not be converted
            data = [self.to_dict(v) for v in obj]
            return data
        elif hasattr(obj, "__dict__"):
            #If its an object that has a __dict__ attribute this can be used
            data = []
            for k, v in obj.__dict__.items():
                #Iterate through all items of the __dict__ and and try converting each value to a dict
                #The resulting key value pairs are stored as tuples in a list that is then converted to a final dict
                data.append((k, self.to_dict(v)))
            return dict(data)
        else:
            return obj

    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def __repr__(self) -> str:
        pass
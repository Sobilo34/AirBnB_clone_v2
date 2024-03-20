#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        def all(self, cls=None):
        """returns a dictionary, and if cls is given, return all objects of that
        class type in a list.
        Return:
            returns a dictionary of __object
        """
        if cls is None:
            return self.__objects
        else:
            if isinstance(cls, str):
                cls = eval("{}".format(cls))
            new_dict = {}
            for k, v in self.__objects.items():
                print("{}: {}".format(k, v))
                if type(v) == cls:
                    print("adding\n")
                    new_dict[k] = v
            return new_dict
        """
        if cls is None:
            return FileStorage.__objects

        filtered = {}
        for key, value in self.__objects.items():
            if isinstance(value, cls):
                filtered[key] = value
        return filtered
        """

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        if obj is None:
            return
        to_delete = None
        for key, value in self.__objects.items():
            if value == obj:
                to_delete = key
                break
        if to_delete is not None:
            del FileStorage.__objects[to_delete]

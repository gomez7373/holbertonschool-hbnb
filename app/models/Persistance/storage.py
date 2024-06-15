"""
This module defines the Storage class for handling data persistence.
"""

import json
import os
from models.user import User
from models.city import City
from models.review import Review
from models.country import Country
from models.place import Place

class Storage:
    """
    Storage class for handling data persistence.
    """
    FILE_NAME = "data.json"
    data = []
    classes = {
            "User": User,
            "City": City,
            "Place":Place,
            "Review": Review,
            "Country": Country
            }

    def new(self, instance):


        Storage.data.append(instance)
    def save(self, instance):
        """Save an entity to a file."""
        prep = []
        for obj in Storage.data:
            prep.append(obj.to_dict())


        with open(Storage.FILE_NAME, 'w') as file:
            json.dump(prep, file, indent=4)


    def delete(self, obj_id):
        """Delete an entity by its ID."""
        for indx, data in enumerate(Storage.data):
            if obj_id in data.to_dict().values():
                return Storage.data.pop(indx)


    def all(self, target=None):
        content = []
        if target:
            for obj in Storage.data:

                if target in obj.to_dict().values():
                    content.append(obj)
            return content

        """Retrieve all entities of a class."""
        return Storage.data

    def load(self):
        try: 
            with open(Storage.FILE_NAME,"r") as file:
                objects = json.load(file)
                for obj in objects:
                    temp = Storage.classes.get(obj["class"])(obj)
                    temp.save()
        except: 
            print("Couldn't load the file.")


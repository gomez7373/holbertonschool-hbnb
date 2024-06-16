"""
This module defines the Storage class for handling data persistence.
"""

import json
import os

class Storage:
    FILE_NAME = "data.json"
    data = []
    classes = {
        "User": None,  # Placeholder
        "City": None,  # Placeholder
        "Place": None,  # Placeholder
        "Review": None,  # Placeholder
        "Country": None  # Placeholder
    }

    def new(self, instance):
        Storage.data.append(instance)

    def save(self):
        prep = []
        for obj in Storage.data:
            prep.append(obj.to_dict())
        with open(Storage.FILE_NAME, 'w') as file:
            json.dump(prep, file, indent=4)

    def delete(self, obj_id):
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
        return Storage.data

    def load(self):
        from app.models.user import User
        from app.models.city import City
        from app.models.review import Review
        from app.models.country import Country
        from app.models.place import Place

        Storage.classes["User"] = User
        Storage.classes["City"] = City
        Storage.classes["Place"] = Place
        Storage.classes["Review"] = Review
        Storage.classes["Country"] = Country
        
        try:
            with open(Storage.FILE_NAME, "r") as file:
                objects = json.load(file)
                for obj in objects:
                    temp = Storage.classes.get(obj["class"])(obj)
                    temp.save()
        except:
            print("Couldn't load the file.")

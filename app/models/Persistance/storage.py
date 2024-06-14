"""
This module defines the Storage class for handling data persistence.
"""

import json
import os

class Storage:
    """
    Storage class for handling data persistence.
    """
    FILE_NAME = "data.json"
    data = []


    def new(self, instance):
        pass
    def save(self, instance):
        """Save an entity to a file."""
        to_save = instance.to_dict()
        to_save['created_at'] = str(to_save['created_at'])
        to_save['updated_at'] = str(to_save['updated_at'])
        with open(Storage.FILE_NAME, 'w') as file:
            json.dump(to_save, file, indent=4)

    def get(self, entity_id):
        """Retrieve an entity by its ID."""
        file_path = os.path.join(self.DATA_DIR, f'{entity_id}.json')
        if not os.path.exists(file_path):
            return None
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data

    def delete(self, entity_id):
        """Delete an entity by its ID."""
        file_path = os.path.join(self.DATA_DIR, f'{entity_id}.json')
        if os.path.exists(file_path):
            os.remove(file_path)
            return True
        return False

    def all(self, cls):
        """Retrieve all entities of a class."""
        entities = []
        for file_name in os.listdir(self.DATA_DIR):
            if file_name.endswith('.json'):
                with open(os.path.join(self.DATA_DIR, file_name), 'r') as file:
                    data = json.load(file)
                    if data.get('id').startswith(cls.__name__):
                        entities.append(cls.from_dict(data))
        return entities

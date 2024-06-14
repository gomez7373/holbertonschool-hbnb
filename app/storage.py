"""
This module defines the Storage class for handling data persistence.
"""

import json
import os

class Storage:
    """
    Storage class for handling data persistence.
    """
    DATA_DIR = os.getenv('DATA_DIR', '/default/path/to/your/data')

    def save(self, entity):
        """Save an entity to a file."""
        if not os.path.exists(self.DATA_DIR):
            os.makedirs(self.DATA_DIR)
        file_path = os.path.join(self.DATA_DIR, f'{entity.id}.json')
        with open(file_path, 'w') as file:
            json.dump(entity.to_dict(), file, indent=4)

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

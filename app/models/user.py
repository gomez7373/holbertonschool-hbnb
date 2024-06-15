"""
This module defines the User class.
"""

import hashlib
import json
import os
from datetime import datetime
from base_model import BaseModel
#from app.models.Persistance.storage import Storage
#from review import Review

class User(BaseModel):
    """
    User model class.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
        #self.password_hash = password_hash or self.hash_password(password)
    places = []
    reviews = []


   # storage = Storage()
    #ID_COUNTER_FILE = os.path.join(storage.DATA_DIR, 'id_counter.txt')
"""
    def __init__(self, email=None, password=None, first_name=None, last_name=None, password_hash=None, user_id=None, places=None, reviews=None):
        #Initialize the user with specific attributes.
        super().__init__()
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        #self.password_hash = password_hash or self.hash_password(password)
        self.user_id = user_id or self.generate_unique_id()
        self.places = places or []
        self.reviews = reviews or []

#----------------------------------------------------------------------------


    def add_place(self, place):
   #Add a place to the user's list of places.
        self.places.append(place)

    def add_review(self, rating, text, place):
        #Add a review to the user's list of reviews.
        if place.host == self:
            return "The owner can't review their own place."
        review = Review(rating=rating, text=text, user=self, place=place)
        self.reviews.append(review)
        place.reviews.append(review)
        return review

   #def hash_password(self, password):
       #Hash the user's password.
        #return hashlib.sha256(password.encode()).hexdigest()

    @classmethod
    def generate_unique_id(cls):
        #Generate a unique user ID.
        #if not os.path.exists(cls.ID_COUNTER_FILE):
            #with open(cls.ID_COUNTER_FILE, 'w') as file:
                #file.write('1000')
        #with open(cls.ID_COUNTER_FILE, 'r+') as file:
            #last_id = int(file.read().strip())
            #new_id = last_id + 1
            #file.seek(0)
            #file.write(str(new_id))
       # return new_id
       #---------------------------------------------------------------

    def save_to_file(self):
    #Save the user to a file.
       # self.storage.save(self)
        pass

    @classmethod
    def get_by_id(cls, user_id):
    #Retrieve a user by their ID.
       # user_data = cls.storage.get(user_id)
        #if user_data:
         #   return cls.from_dict(user_data)
        return None

    #@classmethod
    def update(cls, user_id, **kwargs):
        #Update a user's attributes.
        user = cls.get_by_id(user_id)
        if not user:
            return None
        for key, value in kwargs.items():
            if hasattr(user, key):
                setattr(user, key, value)
        user.save_to_file()
        return user

    @classmethod
    def delete(cls, user_id):
        #Delete a user by their ID.
       # return cls.storage.delete(user_id)
        pass
  #  def to_dict(self):
   #     Convert the user to a dictionary.
    #    return {
     #       'id': self.id,
      #      'created_at': self.created_at.isoformat(),
       #     'updated_at': self.updated_at.isoformat(),
        #    'email': self.email,
         #   'password': self.password,
        #    'first_name': self.first_name,
         #   'last_name': self.last_name,
          #  'password_hash': self.password_hash,
           # 'user_id': self.user_id,
           # 'places': self.places,
            #'reviews': self.reviews
       # }

    @classmethod
    def from_dict(cls, data):
        #Create a user from a dictionary.
        user = cls(
            email=data['email'],
            password=data['password'],
            first_name=data['first_name'],
            last_name=data['last_name'],
            password_hash=data.get('password_hash'),
            user_id=data.get('user_id'),
            places=data.get('places', []),
            reviews=data.get('reviews', [])
        )
        user.id = data['id']
        user.created_at = datetime.fromisoformat(data['created_at'])
        user.updated_at = datetime.fromisoformat(data['updated_at'])
        return user

temp = User()

print(temp.to_dict())

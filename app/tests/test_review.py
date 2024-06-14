"""
This module contains unit tests for the Review model.
"""

import unittest
from app.models.review import Review
from app.models.user import User
from app.models.place import Place

class TestReview(unittest.TestCase):
    """Test cases for the Review model."""

    def test_create_review(self):
        """Test review creation."""
        user = User(email="test@example.com", password="password", first_name="First", last_name="Last")
        place = Place(name="Test Place", city_id="1", host_id="1", number_of_rooms=3, number_of_bathrooms=2, price_per_night=100, max_guests=4)
        review = Review(rating=5, text="Great place!", user=user, place=place)
        self.assertIsNotNone(review.id)
        self.assertEqual(review.rating, 5)

if __name__ == '__main__':
    unittest.main()

"""
This module contains unit tests for the User model.
"""

import unittest
from app.models.user import User

class TestUser(unittest.TestCase):
    """Test cases for the User model."""

    def test_create_user(self):
        """Test user creation."""
        user = User(email="test@example.com", password="password", first_name="First", last_name="Last")
        self.assertIsNotNone(user.id)
        self.assertEqual(user.email, "test@example.com")

if __name__ == '__main__':
    unittest.main()

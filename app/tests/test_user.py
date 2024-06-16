import unittest
from app import create_app  # Import your Flask app factory function

class TestUser(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = create_app()
        cls.app_context = cls.app.app_context()
        cls.app_context.push()
        cls.client = cls.app.test_client()

    @classmethod
    def tearDownClass(cls):
        cls.app_context.pop()

    def test_user_creation(self):
        response = self.client.post('/users', json={'name': 'Test User', 'email': 'test@example.com'})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json, {'message': 'User created'})

if __name__ == '__main__':
    unittest.main()

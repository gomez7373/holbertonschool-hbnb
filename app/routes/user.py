"""
This module defines the routes for managing users.
"""

from flask import Blueprint, request, jsonify
from app.models.user import User

user_bp = Blueprint('users', __name__, url_prefix='/users')
users = []

@user_bp.route('/', methods=['GET'])
def get_users():
    """Retrieve a list of all users."""
    users = User.all(User)
    return jsonify([user.to_dict() for user in users])

@user_bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data or not 'name' in data or not 'email' in data:
        return jsonify({'error': 'Invalid input'}), 400

    # Check if user already exists
    for user in users:
        if user['email'] == data['email']:
            return jsonify({'error': 'User already exists'}), 400

    # Create new user
    new_user = {
        'id': len(users) + 1,
        'name': data['name'],
        'email': data['email']
    }
    users.append(new_user)
    return jsonify({'message': 'User created', 'user': new_user}), 201

@user_bp.route('/<user_id>', methods=['GET'])
def get_user(user_id):
    """Retrieve a specific user by ID."""
    user = User.all(user_id)
    if user:
        return jsonify(user.to_dict())
    return jsonify({'error': 'User not found'}), 404

@user_bp.route('/<user_id>', methods=['PUT'])
def update_user(user_id):
    """Update an existing user."""
    data = request.get_json()
    updated_user = User.update(user_id, **data)
    if updated_user:
        return jsonify(updated_user.to_dict())
    return jsonify({'error': 'User not found'}), 404

@user_bp.route('/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    """Delete a user by ID."""
    if User.delete(user_id):
        return jsonify({'message': 'User deleted successfully'}), 200
    return jsonify({'error': 'User not found'}), 404

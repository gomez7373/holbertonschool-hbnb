"""
This module defines the routes for managing users.
"""

from flask import Blueprint, request, jsonify
from app.models.user import User

user_bp = Blueprint('users', __name__, url_prefix='/users')

@user_bp.route('/', methods=['GET'])
def get_users():
    """Retrieve a list of all users."""
    users = User.all(User)
    return jsonify([user.to_dict() for user in users])

@user_bp.route('/', methods=['POST'])
def create_user():
    """Create a new user."""
    data = request.get_json()
    new_user = User(
        email=data['email'],
        password=data['password'],
        first_name=data['first_name'],
        last_name=data['last_name']
    )
    new_user.save_to_file()
    return jsonify(new_user.to_dict()), 201

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

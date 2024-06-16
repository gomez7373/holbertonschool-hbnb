"""
This module defines the routes for managing cities.
"""

from flask import Blueprint, request, jsonify
from app.models.city import City

city_bp = Blueprint('cities', __name__, url_prefix='/cities')

@city_bp.route('/', methods=['GET'])
def get_cities():
    """Retrieve a list of all cities."""
    temp = City()
    cities = temp.all("City")
    return jsonify([city.to_dict() for city in cities])

@city_bp.route('/', methods=['POST'])
def create_city():
    """Create a new city."""
    data = request.get_json()
    new_city = City(name=data['name'], country_code=data['country_code'])
    new_city.save_to_file()
    return jsonify(new_city.to_dict()), 201

@city_bp.route('/<city_id>', methods=['GET'])
def get_city(city_id):
    """Retrieve a specific city by ID."""
    city = City.all(city_id)
    if city:
        return jsonify(city.to_dict())
    return jsonify({'error': 'City not found'}), 404

@city_bp.route('/<city_id>', methods=['PUT'])
def update_city(city_id):
    """Update an existing city."""
    data = request.get_json()
    updated_city = City.update(city_id, **data)
    if updated_city:
        return jsonify(updated_city.to_dict())
    return jsonify({'error': 'City not found'}), 404

@city_bp.route('/<city_id>', methods=['DELETE'])
def delete_city(city_id):
    """Delete a city by ID."""
    if City.delete(city_id):
        return jsonify({'message': 'City deleted successfully'}), 200
    return jsonify({'error': 'City not found'}), 404

"""
This module defines the routes for managing places.
"""

from flask import Blueprint, request, jsonify
from app.models.place import Place

place_bp = Blueprint('places', __name__, url_prefix='/places')

@place_bp.route('/', methods=['GET'])
def get_places():
    """Retrieve a list of all places."""
    places = Place.storage.all(Place)
    return jsonify([place.to_dict() for place in places])

@place_bp.route('/', methods=['POST'])
def create_place():
    """Create a new place."""
    data = request.get_json()
    new_place = Place(
        name=data['name'],
        city_id=data['city_id'],
        host_id=data['host_id'],
        number_of_rooms=data['number_of_rooms'],
        number_of_bathrooms=data['number_of_bathrooms'],
        price_per_night=data['price_per_night'],
        max_guests=data['max_guests']
    )
    new_place.save_to_file()
    return jsonify(new_place.to_dict()), 201

@place_bp.route('/<place_id>', methods=['GET'])
def get_place(place_id):
    """Retrieve a specific place by ID."""
    place = Place.get_by_id(place_id)
    if place:
        return jsonify(place.to_dict())
    return jsonify({'error': 'Place not found'}), 404

@place_bp.route('/<place_id>', methods=['PUT'])
def update_place(place_id):
    """Update an existing place."""
    data = request.get_json()
    updated_place = Place.update(place_id, **data)
    if updated_place:
        return jsonify(updated_place.to_dict())
    return jsonify({'error': 'Place not found'}), 404

@place_bp.route('/<place_id>', methods=['DELETE'])
def delete_place(place_id):
    """Delete a place by ID."""
    if Place.delete(place_id):
        return jsonify({'message': 'Place deleted successfully'}), 200
    return jsonify({'error': 'Place not found'}), 404

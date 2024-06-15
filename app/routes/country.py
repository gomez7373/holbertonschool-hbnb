"""
This module defines the routes for managing countries.
"""

from flask import Blueprint, request, jsonify
from app.models.country import Country

country_bp = Blueprint('countries', __name__, url_prefix='/countries')

@country_bp.route('/', methods=['GET'])
def get_countries():
    """Retrieve a list of all countries."""
    countries = Country.all()
    return jsonify([country.to_dict() for country in countries])

@country_bp.route('/<code>', methods=['GET'])
def get_country(code):
    """Retrieve a specific country by code."""
    country = Country.all(code)
    if country:
        return jsonify(country.to_dict())
    return jsonify({'error': 'Country not found'}), 404

@country_bp.route('/<code>', methods=['PUT'])
def update_country(code):
    """Update an existing country."""
    country = Country.all(code)
    if not country:
        return jsonify({'error': 'Country not found'}), 404
    data = request.get_json()
    country.update(**data)
    return jsonify(country.to_dict())

@country_bp.route('/<code>', methods=['DELETE'])
def delete_country(code):
    """Delete a country by code."""
    if Country.delete(code):
        return jsonify({'message': 'Country deleted successfully'}), 200
    return jsonify({'error': 'Country not found'}), 404

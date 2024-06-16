"""
This module defines the routes for managing reviews.
"""

from flask import Blueprint, request, jsonify
from app.models.review import Review

review_bp = Blueprint('reviews', __name__, url_prefix='/reviews')

@review_bp.route('/', methods=['GET'])
def get_reviews():
    """Retrieve a list of all reviews."""
    reviews = Review.all(Review)
    return jsonify([review.to_dict() for review in reviews])

@review_bp.route('/', methods=['POST'])
def create_review():
    """Create a new review."""
    data = request.get_json()
    new_review = Review(
        rating=data['rating'],
        text=data['text'],
        user=data['user'],
        place=data['place']
    )
    new_review.save_to_file()
    return jsonify(new_review.to_dict()), 201

@review_bp.route('/<review_id>', methods=['GET'])
def get_review(review_id):
    """Retrieve a specific review by ID."""
    review = Review.all(review_id)
    if review:
        return jsonify(review.to_dict())
    return jsonify({'error': 'Review not found'}), 404

@review_bp.route('/<review_id>', methods=['PUT'])
def update_review(review_id):
    """Update an existing review."""
    data = request.get_json()
    updated_review = Review.update(review_id, **data)
    if updated_review:
        return jsonify(updated_review.to_dict())
    return jsonify({'error': 'Review not found'}), 404

@review_bp.route('/<review_id>', methods=['DELETE'])
def delete_review(review_id):
    """Delete a review by ID."""
    if Review.delete(review_id):
        return jsonify({'message': 'Review deleted successfully'}), 200
    return jsonify({'error': 'Review not found'}), 404

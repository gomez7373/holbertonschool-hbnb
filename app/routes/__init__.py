"""
This module initializes the routes package and registers all route blueprints.
"""

from flask import Blueprint
from app.routes.city import city_bp
from app.routes.country import country_bp
from app.routes.place import place_bp
from app.routes.review import review_bp
from app.routes.user import user_bp

api_bp = Blueprint('api', __name__)

# Register blueprints for different routes
api_bp.register_blueprint(user_bp)
api_bp.register_blueprint(place_bp)
api_bp.register_blueprint(city_bp)
api_bp.register_blueprint(country_bp)
api_bp.register_blueprint(review_bp)

def register_routes(app):
    """
    Register all routes with the Flask application.
    """
    app.register_blueprint(api_bp, url_prefix='/api')

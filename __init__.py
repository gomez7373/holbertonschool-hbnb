"""
This module initializes the Flask application and registers routes.
"""
# holbertonschool-hbnb/__init__.py

print("Loading main __init__.py")

from flask import Flask
from app.routes import register_routes

print("Imports in main __init__.py completed")

def create_app():
    print("Creating app in main __init__.py")
    app = Flask(__name__)
    app.config['DEBUG'] = True  # Enable debug mode

    # Register routes
    register_routes(app)
    print("Routes registered in main __init__.py")

    return app

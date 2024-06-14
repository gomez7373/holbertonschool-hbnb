# holbertonschool-hbnb/app/routes/__init__.py

from flask import Flask, jsonify
from .user import user_bp
from .review import review_bp
from .place import place_bp
from .country import country_bp
from .city import city_bp

def register_routes(app: Flask):
    @app.route('/')
    def index():
        return jsonify({"message": "Welcome to the HBnB API!"})

    print("Registering user routes")
    app.register_blueprint(user_bp)
    print("User routes registered")

    print("Registering review routes")
    app.register_blueprint(review_bp)
    print("Review routes registered")

    print("Registering place routes")
    app.register_blueprint(place_bp)
    print("Place routes registered")

    print("Registering country routes")
    app.register_blueprint(country_bp)
    print("Country routes registered")

    print("Registering city routes")
    app.register_blueprint(city_bp)
    print("City routes registered")

    print("All routes registered successfully")

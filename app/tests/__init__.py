from flask import Flask

def create_app():
    app = Flask(__name__)

    # Register Blueprints
    from app.routes.user import user_bp
    app.register_blueprint(user_bp)

    return app

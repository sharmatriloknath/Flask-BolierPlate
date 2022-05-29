from flask import Flask
from app.config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Register BluePrints
    from app.main.routes import main
    app.register_blueprint(main)

    return app


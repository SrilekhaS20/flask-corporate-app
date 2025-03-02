from flask import Flask
from config import Config
import logging

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    from app.routes import main
    app.register_blueprint(main)

    return app
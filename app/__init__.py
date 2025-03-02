from flask import Flask
from config import Config
from app.routes import main
from app.utils.error_handler import register_error_handlers

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    from app.routes import main
    app.register_blueprint(main)
    register_error_handlers(app)

    return app
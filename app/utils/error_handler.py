from flask import jsonify
import traceback
from app.utils.logger import logger

def register_error_handlers(app):
    @app.errorhandler(404)
    def not_found_error(error):
        response = {
            "error": "Not Found",
            "message": "The requested resource was not found."
        }
        logger.warning(f"404 Not Found: {error}")
        return jsonify(response), 404

    @app.errorhandler(500)
    def internal_server_error(error):
        response = {
            "error": "Internal Server Error",
            "message": "An unexpected error occurred."
        }
        logger.error(f"500 Internal Error: {traceback.format_exc()}")
        return jsonify(response), 500
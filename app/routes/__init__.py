from flask import Blueprint

main = Blueprint('main', __name__)

from app.routes import health
from app.routes import home
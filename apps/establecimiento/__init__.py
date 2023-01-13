from flask import Blueprint
establecimiento = Blueprint('establecimiento', __name__, template_folder= 'templates', static_folder='static' )
from . import routes


from flask import Blueprint
ingresos = Blueprint('ingresos', __name__, template_folder= 'templates', static_folder='static')
from . import routes
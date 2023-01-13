from flask import Flask
from config.db import db
from apps.users import users
from apps.ingresos import ingresos
from apps.login import login
from apps.establecimiento import establecimiento
from config.settings import config

def create_app():
    app = Flask(__name__)
    app.config.from_object(config['developer'])
    # app.config['SECRET_KEY'] ='7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # postgresql:postgresql//<nombre_usuario>:<password>@<host>:<puerto>/<nombre_basededatos>
    db.init_app(app)
    app.register_blueprint(login)
    app.register_blueprint(establecimiento)
    app.register_blueprint(users)
    app.register_blueprint(ingresos)
    return app

from flask_login import LoginManager, UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

# from base.model_mixin.models import AbstractUser
from config.db import db
from base.contrib.models import BaseModelMixin, RelationShipAudit

class User(BaseModelMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # is_admin = db.Column(db.Boolean, default=False)
    # is_superuser = db.Column(db.Boolean, default=False)
    is_active = db.Column(db.Boolean, default=True)
    rol = db.Column(db.Integer, nullable= True)
    #1 administrador, 2 gestor, 3 superuser
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(256), nullable=False)
    first_name = db.Column(db.String(100), nullable=True)
    last_name = db.Column(db.String(100), nullable=True)
    correo = db.Column(db.String(200), nullable=True, default='sininfo@gmail.com')
    establecimiento_id = db.Column(db.Integer, db.ForeignKey('establecimiento.id'), nullable=True)
    user_create = db.Column(db.Integer, nullable= True, default = None)
    user_modified = db.Column(db.Integer, nullable=True, default = None)

    def __init__(self, is_active, rol, username, password, first_name, last_name, correo, establecimiento, user_create):
        self.is_active = is_active
        self.rol = rol
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.correo = correo
        self.establecimiento_id = establecimiento
        self.user_create = user_create


    def get_id(self):
        return str(self.id)
        # return str(User.query.get(id).id)

    @classmethod
    def get_by_id(cls):
        return User.query.get(id)

    @classmethod
    def set_password(self, password):
        pw = generate_password_hash(password)
        return pw

    @classmethod
    def check_password(self, hash_pw, password):
        pw = check_password_hash(hash_pw, password)
        return pw

# class Rol(db.Model):
#   id = db.Column(db.Integer, primary_key=True)
#   codigo = db.Column(db.Integer, nullable=False)
#   user = db.relationship('rol', backref='user')
#   name_rol = db.Column(db.String, nullable=True)
#

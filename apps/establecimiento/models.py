from sqlalchemy import null
from config.db import db
import datetime
from base.contrib.models import BaseModelMixin, RelationShipAudit

class Establecimiento(BaseModelMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(40), nullable = False)
    direccion = db.Column(db.String(50), nullable = False)
    telefono = db.Column(db.String(10), nullable = False)
    observacion = db.Column(db.String(200), nullable=True)
    foto = db.Column(db.String(200), nullable=True)
    user = db.relationship('User', backref='establecimiento')
    user_create = db.Column(db.Integer, nullable= True, default= None)
    user_modified = db.Column(db.Integer, nullable=True, default= None)
    is_active = db.Column(db.Boolean, default=True)

    def __init__(self, nombre, direccion, telefono, observacion, foto, user_create, is_active):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.observacion = observacion
        self.foto=foto
        self.is_active=is_active
        self.user_create=user_create

    # @staticmethod
    # def get_by_id(id):
    #     return establecimiento.query.filter_by(id=id).first()




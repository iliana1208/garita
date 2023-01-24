from sqlalchemy import null
from config.db import db
import datetime
from base.contrib.models import BaseModelMixin, RelationShipAudit

class Establecimiento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(40), nullable = False)
    direccion = db.Column(db.String(50), nullable = False)
    telefono = db.Column(db.String(10), nullable = False)
    fecha_creacion = db.Column(db.DateTime, nullable= True)
    observacion = db.Column(db.String(200), nullable=True)
    foto = db.Column(db.String(200), nullable=True)
    user = db.relationship('User', backref='establecimiento')
    # @staticmethod
    # def get_by_id(id):
    #     return establecimiento.query.filter_by(id=id).first()




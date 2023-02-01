from sqlalchemy import null
from config.db import db
import datetime
from base.contrib.models import BaseModelMixin, RelationShipAudit

class Ingreso(BaseModelMixin, RelationShipAudit, db.Model):
    # __abstract__=True
    id = db.Column(db.Integer, primary_key=True)
    fecha_ingreso = db.Column(db.DateTime, default=datetime.datetime.now())
    nombre = db.Column(db.String(40), nullable = False)
    placa = db.Column(db.String(10), nullable = False)
    cedula = db.Column(db.String(10), nullable = False)
    fecha_salida= db.Column(db.DateTime, nullable= True)
    tiempo = db.Column(db.Integer, nullable= True)
    is_active = db.Column(db.Boolean, default=True)

    def __init__(self, nombre, placa, cedula, is_active):
        self.nombre = nombre
        self.placa = placa
        self.cedula = cedula
        self.is_active = is_active

    # user_creation = db.Column(db.Integer, db.ForeignKey('user.id'), nullable= True)
    # user_modified = db.Column(db.Integer, db.ForeignKey('user.id'), nullable= True)

    # @staticmethod
    # def get_by_id(id):
    #     return ingreso.query.filter_by(id=id).first()


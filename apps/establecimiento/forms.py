import wtforms
from flask_wtf import FlaskForm
from wtforms.validators import length, email, DataRequired

class EstablecimientoForm(FlaskForm):
    nombre = wtforms.StringField(label='Nombre', validators=[DataRequired(message='El dato es requerido')],
                                 render_kw={'placeholder': 'Nombre del establecimiento', 'class': 'form-control'})
    direccion = wtforms.StringField(label='Dirección', validators=[DataRequired(message='El dato es requerido')],
                                render_kw={'placeholder': 'Dirección', 'class': 'form-control'})
    telefono = wtforms.StringField(label='Teléfono', validators=[length(9, 10, message='El número de cedula debe tener 10 dígitos'),DataRequired(message='El dato es requerido')],
                                 render_kw={'placeholder': 'Teléfono', 'class': 'form-control'})
    observacion = wtforms.StringField(label='Observación',
                                    render_kw={'placeholder': 'Observación',
                                               'class': 'form-control'})
    guardar = wtforms.SubmitField('Enviar',
                                  render_kw={'class':'btn btn-primary btn-block'})

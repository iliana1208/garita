import wtforms
from flask_wtf import FlaskForm
from wtforms.validators import length, email, DataRequired


class IngresoForm(FlaskForm):
    nombre = wtforms.StringField(label='Nombre', validators=[DataRequired(message='El dato es requerido')],
                                 render_kw={'placeholder': 'Nombre del visitante', 'class': 'form-control'})
    placa = wtforms.StringField(label='Placa', validators=[DataRequired(message='El dato es requerido')],
                                render_kw={'placeholder': 'Placa del vehiculo del visitante', 'class': 'form-control'})
    cedula = wtforms.StringField(label='Cedula', validators=[length(10, 10, message='El número de cedula debe tener 10 dígitos'),DataRequired(message='El dato es requerido')],
                                 render_kw={'placeholder': 'Cedula del visitante', 'class': 'form-control'})
    guardar = wtforms.SubmitField('Enviar',
                                  render_kw={'class':'btn btn-primary btn-block'})


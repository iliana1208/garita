import wtforms
from flask_wtf import FlaskForm
from wtforms.validators import length, email, DataRequired

class LoginForm(FlaskForm):
    username = wtforms.StringField(label='Username',
                                   validators=[DataRequired(message='Dato es requerido'), length(min=4, max=10)],
                                   render_kw={'placeholder':'Ingrese su nombre de usuario', 'class':'form-control'})
    password = wtforms.PasswordField(label='Password', validators=[DataRequired(message='Dato es requerido')],
                                     render_kw={'placeholder': 'Ingrese su contraseña', 'class': 'form-control'})
    remember_me = wtforms.BooleanField(label='Recuérdame',
                                       render_kw={'class': 'icheck-primary'})

    rol = wtforms.SelectField(choices=[(1,'Administrador'), (2,'Superuser'),(3,'Gestor')], render_kw={'class': 'btn btn-primary btn-block'})
    guardar = wtforms.SubmitField('Iniciar sesión', render_kw={'class': 'btn btn-primary btn-block'})

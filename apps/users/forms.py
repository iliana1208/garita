import wtforms
from flask_wtf import FlaskForm
from wtforms.validators import length, email, DataRequired

class RegistrosForm(FlaskForm):
    first_name = wtforms.StringField(label="Nombres", validators=[length(max=100, min=1), DataRequired()],
                                     render_kw={'placeholder': 'Ingrese sus nombres', 'class': 'form-control'})
    last_name = wtforms.StringField(label="Apellidos", validators=[length(max=100, min=1), DataRequired()],
                                    render_kw={'placeholder': 'Ingrese sus apellidos', 'class': 'form-control'})

    username = wtforms.StringField(label="Username", validators=[length(max=20, min=4), DataRequired()],
                                   render_kw={'placeholder': 'Ingrese su username', 'class': 'form-control'})
    rol = wtforms.SelectField(choices=[(1, 'Administrador'), (2, 'Gestor'), (3, 'Superuser'),],
                              render_kw={'class': 'btn btn-primary btn-block'})
    establecimiento = wtforms.SelectField(choices=[(0, "-----")], coerce=int,
                                          render_kw={'class': 'btn btn-primary btn-block'})
    password = wtforms.PasswordField(label="Password", validators=[length(max=30, min=4), DataRequired()],
                                     render_kw={'placeholder': 'Ingrese su contraseña', 'class': 'form-control'})
    email = wtforms.EmailField(label="Correo electronico",
                               validators=[email(message="Correo no cumple con el formato requerido")],
                               render_kw={'placeholder': 'Ingrese su correo', 'class': 'form-control'})
    register = wtforms.SubmitField('Registrarse', render_kw={'class': 'btn btn-primary btn-block'})

    def __init__(self, *args, **kwargs):
        super(RegistrosForm, self).__init__(*args, **kwargs)
        pass

    def change_choices_estbl(self, lista):
        self.establecimiento.choices = lista

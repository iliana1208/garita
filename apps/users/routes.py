from flask import request, redirect, url_for, render_template, flash
from flask_login import current_user

from apps.users import users
from apps.users.forms import RegistrosForm
from apps.users.models import User
from config.db import db

@users.route('/registros', methods = ['GET', 'POST'])
def registros():
    if current_user.is_authenticated:
        return redirect(url_for("ingresos.listado"))
    method = request.method
    form = RegistrosForm()
    error = ""

    if method == 'POST':
        try:
            if form.validate_on_submit():
                username = form.username.data
                password = form.password.data
                first_name = form.first_name.data
                last_name = form.last_name.data
                email = form.email.data
                is_active = True
                establecimiento = form.establecimiento.data
                rol = form.rol.data
                user = User.query.filter_by(username=username).first()
                if not user:
                    try:

                        user = User(username=username, password=password, first_name=first_name, last_name=last_name, is_active=is_active,
                                    rol=rol, establecimiento=establecimiento,  correo=email)

                        user.password = User.set_password(password)
                        db.session.add(user)
                        db.session.commit()
                        return redirect(url_for('login.login'))
                    except Exception as e:
                        print('Error', str(e))
                        flash(str(e))

                else:
                    flash("El usuario ingresado ya existe")
            else:
                print("errores", form.errors)
        except Exception as e:
            print("Error", str(e))


    return render_template('registros.html', form=form, title='Registros de nuevos usuarios', error=error)

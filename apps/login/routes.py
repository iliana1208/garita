from flask import redirect, request, url_for, flash, render_template
from flask_login import current_user, login_user, logout_user

from apps.login import login as lg
from werkzeug.urls import url_parse
from apps.users.models import User
from apps.login.forms import LoginForm





@lg.route('/login', methods=['GET', 'POST'])
def login():
    # if current_user.is_authenticated:
    #     return redirect(url_for("ingresos.listado"))
    method = request.method
    form = LoginForm()
    error = ""
    if method == 'POST':
        if form.validate_on_submit():
            username = form.username.data
            password = form.password.data
            rol = form.rol.data
            user = User.query.filter_by(username=username).first()
            if user:
                next_page = request.args.get('next')
                if user.is_active:
                    if user.check_password(user.password, password) and user.rol == int(rol):
                        login_user(user=user, remember=form.remember_me)
                        if not next_page or url_parse(next_page).netloc != '':
                            next_page = url_for("ingresos.listado")
                            return redirect(next_page)
                        else:
                            return redirect(next_page)
                    else:
                        flash("Credenciales incorrectas, intente nuevamente", category='warning')
                else:
                    flash("El usuario está desactivado", category='warning')

            else:
                flash("Credenciales incorrectas, intente nuevamente", category='danger')

        else:
            print(form.errors)

    return render_template("login.html", form=form)

# @lg.route('/')
# def raiz():
#     return redirect(url_for('login'))

@lg.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login.login'))

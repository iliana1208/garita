from flask import request, redirect, url_for, render_template, flash
from flask_login import current_user
import json
from flask import Response
from apps.users.models import User
from apps.users import users
from apps.users.forms import RegistrosForm
from apps.users.models import User
from config.db import db

@users.route('/registro', methods=['GET', 'POST'])
def registro():
    if current_user.is_authenticated:
        return redirect(url_for("ingresos.listado"))

    method = request.method
    form = RegistrosForm()
    lista = [(x.id, x.nombre) for x in User.query.all()]
    form.change_choices_estbl(lista)
    error = ""
    if method == 'GET':
        pass

    if method == 'POST':
        try:
            datos = request.form
            action = datos.get('action')
            if action == 'searchdata':
                list = {}
                try:
                    data = User.query.all()
                    list= []
                    for items in data:
                        list.append(
                            {'id':items.id, 'username': items.username, 'email':items.email,
                             'rol': items.rol, 'opciones':''}
                        )
                except Exception as e:
                    list['error'] = str(e)
                return Response(json.dumps(list))

            form = RegistrosForm()
            if form.validate_on_submit():
                username = request.form.get('username')
                password = request.form.get('password')
                first_name = request.form.get('first_name')
                last_name = request.form.get('last_name')
                email = request.form.get('email')
                is_active = True
                establecimiento = request.form.get('establecimiento')
                rol = request.form.get('rol')
                user = User.query.filter_by(username=username).first()
                if not user:
                    try:

                        user = User(username=username, password=password, first_name=first_name, last_name=last_name,
                                    is_active=is_active,
                                    rol=rol, establecimiento=establecimiento, correo=email)

                        user.password = User.set_password(password)
                        db.session.add(user)
                        db.session.commit()
                        return redirect(url_for('establecimiento.principal'))
                    except Exception as e:
                        print('Error', str(e))
                        flash(str(e))
                else:
                    flash("El usuario ingresado ya existe")
            else:
                print("errores", form.errors)
        except Exception as e:
            print("Error", str(e))

    return render_template('registro.html', form=form, title='Registros de nuevos usuarios', error=error)


@users.route('/edituser/<int:id>', methods=['GET', 'POST'])
def edituser(id):
    method = request.method
    userold = User.query.filter_by(id=id).first()
    user = User.query.get(id)
    form = RegistrosForm(obj=user)
    if method == 'GET':
        pass
        # return Response(response=json.dumps(dic), content_type="application/json")
    elif method == "POST":
        if form.validate_on_submit():
            username = request.form.get('username')
            password = request.form.get('password')
            first_name = request.form.get('first_name')
            last_name = request.form.get('last_name')
            email = request.form.get('email')
            establecimiento = request.form.get('establecimiento')
            rol = request.form.get('rol')

            userold.username = username
            userold.password = password
            userold.first_name = first_name
            userold.last_name = last_name
            userold.email = email
            userold.establecimiento = establecimiento
            userold.rol = rol
            db.session.commit()

        #print("formulario", form.data)
    return render_template("edituser.html", form=form)


@users.route('/userdelete/<int:id>', methods=['GET', 'POST'])
def userdelete(id):
    method = request.method
    user = User.query.get(id)
    form = RegistrosForm(obj=user)
    if method == 'GET':
        userr = User.query.filter_by(id=id).first()
        userr.is_active = False
        db.session.commit()
        response={'status':200}
        return Response(json.dumps(response), content_type="application/json")

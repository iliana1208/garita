from flask import request, redirect, url_for, render_template, flash
from flask_login import current_user
from flask import Response
import json
from apps.establecimiento import *
from apps.establecimiento.models import Establecimiento
from apps.establecimiento.forms import EstablecimientoForm
from config.db import db
from apps.establecimiento import establecimiento as estbl

@estbl.route('/principal', methods=['GET', 'POST'])
def principal():
    form = EstablecimientoForm()
    method = request.method
    if method == 'GET':
        pass

    elif method == 'POST':
        datos = request.form
        action = datos.get('action')
        id_estbl = datos.get('id')
        if action == 'searchdata':
            list = {}
            try:
                data = Establecimiento.query.all()
                list = []
                for items in data:
                    list.append(
                        {'id': items.id, 'nombre': items.nombre, 'direccion': items.direccion,
                         'telefono': items.telefono,
                         'observacion': items.observacion, 'opciones': ''})

            except Exception as e:
                list['error'] = str(e)
            return Response(json.dumps(list))

        form = EstablecimientoForm()
        if form.validate_on_submit():
            nombre = request.form.get('nombre')
            direccion = request.form.get("direccion")
            telefono = request.form.get("telefono")
            observacion = request.form.get("observacion")
            try:
                elemento = Establecimiento(nombre=nombre, direccion=direccion, telefono=telefono,
                                           observacion=observacion)
                db.session.add(elemento)
                db.session.commit()
                print('guardado')
                return redirect(url_for('establecimiento.principal'))
            except Exception as e:
                print('Error', str(e))

    return render_template('principal.html', form=form)


@estbl.route('/edit/<int:id>', methods=['GET', 'POST'])
def editar(id):
    method = request.method
    estblold = Establecimiento.query.filter_by(id=id).first()
    estble = Establecimiento.query.get(id)
    form = EstablecimientoForm(obj=estble)
    # action = estble.get('action')
    if method == 'GET':
        pass
        # return Response(response=json.dumps(dic), content_type="application/json")
    elif method == "POST":
        # form.formdata = request.form.get("form")
        # print("form", request.form.get("form"))
        #print("request.form", request.form)
        if form.validate_on_submit():
            nombre = request.form.get("nombre")
            direccion = request.form.get("direccion")
            telefono = request.form.get("direccion")
            observacion = request.form.get('observacion')
            estblold.nombre = nombre
            estblold.direccion = direccion
            estblold.telefono = direccion
            estblold.observacion = observacion
            db.session.commit()

        #print("formulario", form.data)
    return render_template("edit.html", form=form)


@estbl.route('/estbldelete/<int:id>', methods=['GET', 'POST'])
def estbldelete(id):
    method = request.method
    estble = Establecimiento.query.get(id)
    form = EstablecimientoForm(obj=estble)
    if method == 'GET':
        estbl = Establecimiento.query.filter_by(id=id).first()
        estbl.observacion = 'false'
        db.session.commit()
        response={'status':200}
        # return redirect(url_for('establecimiento.principal'))
        # data = {
        #     # 'redirect': url_for('establecimiento.principal')
        # }
        return Response(json.dumps(response), content_type="application/json")
    # estbl.observacion = 'False'
    #
    # if method == "GET":
    #     pass
    # elif method == "POST":
    #     pass


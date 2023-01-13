from flask import request, redirect, url_for, render_template, flash
from flask_login import current_user
from flask import Response
import json
from apps.establecimiento import *
from apps.establecimiento.models import Establecimiento
from apps.establecimiento.forms import EstablecimientoForm
from config.db import db
from apps.establecimiento import establecimiento as estbl

@estbl.route('/principal',methods=['GET', 'POST'])
def principal():
    method = request.method
    form = EstablecimientoForm()
    if method == 'GET':
        if form.validate_on_submit():
            print("Ingreso es valido")
            # nombre = request.args.get('nombre')
            nombre = form.nombre.data
            direccion = request.args.get("direccion")
            telefono = request.args.get("telefono")
            observacion = request.args.get("observacion")
            try:
                elemento = Establecimiento(nombre=nombre, direccion=direccion, telefono=telefono, observacion=observacion)
                db.session.add(elemento)
                db.session.commit()
                return redirect(url_for('ingresos.listado'))
            except Exception as e:
                print('Error', str(e))
        else:
            print(form.errors)
        return render_template('principal.html', form =form)


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
                        {'id': items.id, 'nombre': items.nombre, 'cedula': items.direccion, 'telefono': items.telefono,
                         'observacion': items.observacion})

            except Exception as e:
                list['error'] = str(e)
            return Response(json.dumps(list))



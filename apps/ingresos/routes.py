from datetime import datetime
from flask import render_template, request, redirect, url_for, flash
from flask import Response
import json
from flask import abort
from apps.ingresos import ingresos
from flask_login import current_user,login_required
from apps.ingresos.forms import IngresoForm
from apps.ingresos import ingresos as entrada
from apps.ingresos.models import Ingreso
from config.db import db

def escala_time(tiempo):
    valor = ''
    if 0 <= tiempo < 60:
        tiempo = tiempo
        valor = str(int(tiempo)) + ' segundos'
    elif 60 <= tiempo < 3600:
        tiempo = tiempo / 60
        valor = str(int(tiempo)) + ' minutos'
    elif 3600 <= tiempo < 86400:
        tiempo = tiempo / 3600
        valor = str(int(tiempo)) + ' horas'
    elif 86400 <= tiempo < 604800:
        tiempo = tiempo / 86400
        valor = str(int(tiempo)) + ' dias'
    elif tiempo > 604800:
        tiempo = tiempo / 604800
        valor = str(int(tiempo)) + ' semanas'
    return valor


@entrada.route('/listado',methods=['GET', 'POST'])
def listado():
    method = request.method
    if method == 'GET':
        return render_template('listado.html')

    if method == 'POST':
        datos = request.form
        action = datos.get('action')
        id_car = datos.get('id')

        if action == 'searchdata':
            print('search')
            list = {}
            try:
                car = Ingreso.query.all()
                # if current_user.rol == 1:
                #     car = [Ingreso.query.filter_by(current_user.establecimiento)]
                list = []
                for items in car:
                    if items.tiempo != None:
                        fecha_ingreso = items.fecha_ingreso.strftime("%d-%m-%Y %H:%M:%S")
                        fecha_salida = items.fecha_salida.strftime("%d-%m-%Y %H:%M:%S")
                        tiempo = escala_time(items.tiempo)
                        #user_modified = current_user.username
                        list.append(
                            {'id': items.id, 'nombre': items.nombre, 'cedula': items.cedula, 'placa': items.placa,
                             'fecha_ingreso': fecha_ingreso,'fecha_salida': fecha_salida, 'tiempo': tiempo})

            except Exception as e:
                list['error'] = str(e)
            return Response(json.dumps(list))


@entrada.route('/ingresos', methods=['GET', 'POST'])
def ingresos():
    method = request.method
    form = IngresoForm()
    if method == 'POST':
        if form.validate_on_submit():
            nombre = request.form.get("nombre")
            placa = request.form.get("placa")
            cedula = request.form.get("cedula")
            try:
                car = Ingreso(nombre=nombre, placa=placa, cedula=cedula, is_active=True)
                db.session.add(car)
                db.session.commit()
            except Exception as e:
                print('Error', str(e))

            return redirect(url_for('ingresos.salidas'))
        else:
            print('El formulario no es valido')

    return render_template('ingresos.html', form=form)


@entrada.route('/salidas', methods=['GET', 'POST'])
def salidas():
    method = request.method
    # form = ''
    # page = int(request.args.get('page', 1))
    # post_pagination = ingreso.all_paginated(page, 10)
    if method == 'GET':
        return render_template('salidas.html')

    if method == 'POST':
        datos = request.form
        action = datos.get('action')
        id_car = datos.get('id')
        print(id_car)
        fecha_actual = datetime.now()
        if action == 'update':
            car = Ingreso.query.filter_by(id=id_car).first()
            car.fecha_salida = fecha_actual

            tiempo = car.fecha_salida-car.fecha_ingreso
            tiempo = round(tiempo.total_seconds())
            car.tiempo = tiempo

            db.session.add(car)
            db.session.commit()

            data = {
                'redirect': url_for('ingresos.listado')
            }
            return Response(json.dumps(data), content_type="application/json")
            # data = {'message': 'ok'}
            # return Response(json.dumps(data))

        if action =='searchdata':
            list = {}
            try:
                car = Ingreso.query.all()
                list = []
                for items in car:
                    if items.tiempo == None:
                        fecha_ingreso = items.fecha_ingreso.strftime("%d-%m-%Y %H:%M:%S")
                        list.append({'id':items.id,'nombre': items.nombre, 'cedula': items.cedula, 'placa': items.placa, 'fecha_ingreso': fecha_ingreso, 'opciones':''})
                        # list.append({'nombre':'Iliana', 'cedula': '0941964694', 'placa':'placa', 'fecha_ingreso':'2022/07/07', 'opciones':'sds'})
            except Exception as e:
                list['error'] = str(e)
            return Response(json.dumps(list))




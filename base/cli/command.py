import click
from app import app

from config.db import db


@app.cli.command("createsuperuser")
def create_user():
    print("hola")
    from apps.users.models import User
    username = click.prompt("username")
    click.echo(username)
    correo = click.prompt("correo")
    click.echo(correo)
    password = click.prompt("password")
    user = User(username=username, password=password, is_active=True, rol=1, first_name='', last_name='',
                correo=correo, establecimiento='')
    user.password = User.set_password(password)
    db.session.add(user)
    db.session.commit()

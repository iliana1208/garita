from apps.users.models import User
from apps.ingresos.models import Ingreso
from apps.establecimiento.models import Establecimiento

from config.app import create_app
from flask_login import LoginManager, current_user
from flask_migrate import Migrate
from config.db import db

app = create_app()
login_manager = LoginManager(app)
# Login_manager Esta clase contiene la lógica para cargar un usuario
# a partir del ID guardado en la sesión o redirigir a los
# usuarios que no están autenticados a la página de login
# cuando intentan acceder a una vista protegida.
login_manager.login_view = 'login'
#El usuario se dirige a login en vez de la pagina 404?? no funcionaa!!!

login_manager.init_app(app)
migrate = Migrate(app, db)

#callback llamado por el metodo user_loader del objeto login_manager
#el callback toma como parametro un stirng con el id del usuario y
# debe devolver el objeto User o None si ID no es valido.

@login_manager.user_loader
def load_user(id):
    return User.query.get(id)

# with app.app_context():
#     db.create_all()

if __name__ == '__main__':
    app.run()

import base.cli.command
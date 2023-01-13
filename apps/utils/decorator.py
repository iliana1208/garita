from flask_login import current_user, LoginManager

from functools import wraps
login_manager = LoginManager()

def login_required(role="ANY"):
    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):
            if not current_user.is_authenticated():
              return login_manager.unauthorized()
            if ((current_user.role != role) and (role != "ANY")):
                return login_manager.unauthorized()
            return fn(*args, **kwargs)
        return decorated_view
    return wrapper

# app.route('/school/')
# @login_required(role="SCHOOL")
# def restricted_view_for_school():
#     pass


# https://stackoverflow.com/questions/15871391/implementing-flask-login-with-multiple-user-classes/15884811#15884811
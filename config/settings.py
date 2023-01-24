from config.constantes import UPLOAD_FOLDER

class Config(object):
    DEBUG = True
    # SERVER_NAME = 'localhost:6000'
    SECRET_KEY = 'ISIksksk212kskdD'
    UPLOAD_FOLDER = UPLOAD_FOLDER
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASK_APP = 'app.py'

class Developer(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///proyect.db'

class Productions(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///prodct.db'

class Test(Config):
    pass

config = {
    'developer': Developer,
    'productions': Productions,
    'test': Test,
}


# project/config.py

import os
basedir = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))

class BaseConfig(object):
    SECRET_KEY = 'my_precious'
    DEBUG = True
    BCRYPT_LOG_ROUNDS = 13
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'mydatabase.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

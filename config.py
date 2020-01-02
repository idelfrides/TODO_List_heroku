'''
DEBUG = True

import os.path
base_dir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(base_dir, 'todolist_db.db')
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = b'\xdd\x8b\xad\x13\xf8\xda-\xfd\xa2c\\B\x1a\xed4\xb1'
'''
# ------------------------------------------------------

DEBUG = False

import os.path


SQLALCHEMY_TRACK_MODIFICATIONS = True
# SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
# SECRET_KEY = os.environ.get('SECRET_KEY')


# heroku config:set PYTHONPATH=TODO_List_heroku
# base_dir = os.path.abspath(os.path.dirname(__file__))

    # gem 'activerecord-postgresql-adapter'
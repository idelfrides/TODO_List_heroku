from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_login import LoginManager
import os


app = Flask(__name__)

app.config.from_object('config')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

db = SQLAlchemy(app)

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

login_manager = LoginManager(app)

'''
def getDB():
    return db
'''
def getApp():
    return app

from app.models import tables, forms
from app.controllers import default

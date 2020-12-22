from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
'''
testing account is CoreyMSchafer1@gmail.com and password is testing

'''


app = Flask(__name__)
app.config['SECRET_KEY']='3090657a7c7bbbfebf02f365802085fe'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db' #/// for relative location
db=SQLAlchemy(app)
bcrypt=Bcrypt(app)
login_manager= LoginManager(app)
login_manager.login_view= 'login'
login_manager.login_message_category = 'info'

from flaskblog import routes #imported at lst to skip the circular import because routes need app=Flask(__name__) variable
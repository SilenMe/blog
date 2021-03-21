from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
import os #for env var
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
#email config
app.config['MAIL_SERVER']='smtp.googlemail.com'
app.config['MAIL_PORT']=587
app.config['MAIL_USE_TLS']=True
app.config['MAIL_USERNAME']=os.environ.get('EMAIL_USER') # change this for security in os.environment

app.config['MAIL_PASSWORD']=os.environ.get('EMAIL_PASS')
mail=Mail(app)

from flaskblog import routes #imported at lst to skip the circular import because routes need app=Flask(__name__) variable
# flask blog app

to run the app first complete the requirments given in requirment.txt then run the flaskblog.py

used flask-wtf for form validation. At first the name sound the funny but it's really life-saving. For more info visit https://flask-wtf.readthedocs.io/.

used wtForms for form validation. wtforms removed email-validation you you have saperetely install/import 'pip install email_validator'

used sqlalchemy ORM(object relational mapper) because it work fine with all databases.

tree /f





### initial database setup on devlopment machine using sqlite
from flaskblog import db
db.create_all()
from flaskblog import User, Post (after migration from flaskblog.models import User, Post)
user_1=User(username='silenme',email='silen@silenme.com',password='pwd')
db.session.add(user_1)
db.session.commit()

used flask-login for login and authentication

used Image class of Pillow(PIL) module so that image(profile pic) get rezised before uploading (pip/pip3 install Pillow) version 7.0.0 which I have used


dont forget to paginate because it will help in speed and reliebility
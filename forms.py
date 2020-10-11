# this file will be used as form for our app which is based on flask-wtf
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm): #using flaskform as a parent class
	username=StringField('Username',validators=[DataRequired(), Length(min=2,max=20)])
	email=StringField('Email',validators=[DataRequired(), Email()])
	password=PasswordField('Password',validators=[DataRequired()])
	confirm_password=PasswordField('Confirm Password',validators=[DataRequired(), EqualTo('password')])
	submit=SubmitField('Sign Up')

class LoginForm(FlaskForm): #using flaskform as a parent class
	email=StringField('Email',validators=[DataRequired(),Email()]) #using email for login
	password=PasswordField('Password',validators=[DataRequired()])
	remember=BooleanField('Remember Me') #needs an assosiate cookies
	submit=SubmitField('Sign Up')

		
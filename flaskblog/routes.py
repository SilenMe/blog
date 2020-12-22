from flask import render_template, url_for, flash, redirect, request
from flaskblog import app, db, bcrypt
from flaskblog.forms import RegistrationForm, LoginForm 
from flaskblog.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required


posts=[
{
	'author':'abc',
	'title':'title 1',
	'content':'content 1',
	'date_posted':'date_posted 1'
},
{
	'author':'abcd',
	'title':'title 2',
	'content':'content 2',
	'date_posted':'date_posted 2'
}
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',posts=posts) #posts=posts tell that, we can use 'posts' variale (which is defined here) as 'posts' in any templates

@app.route('/about')
def about():
    return render_template('about.html',title='About')

@app.route('/register',methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form=RegistrationForm()
    if form.validate_on_submit():
        hashed_password= bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user=User(username=form.username.data,email=form.email.data,password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Account has been created.', 'success')
        return redirect(url_for('home'))
    return render_template('register.html',title='Register', form=form)
    
@app.route('/login',methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form=LoginForm()
    if form.validate_on_submit():
        user=User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user,remember=form.remember.data)
            next_page = request.args.get('next') # http://website/login?next=%2Faccount used to solve that ?next... request, note that args is a dict so used get methode to skip any error
            return redirect(next_page) if next_page else redirect(url_for('home'))

        else:
            flash('Login unsuccesful. Check email and password','danger') #danger bootstrap class will pop texk as color red
    return render_template('login.html',title='Login', form=form)

@app.route("/logout")    
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/account")   
@login_required #if not login then dont go to this page 
def account():
    return render_template('account.html',title='Account')
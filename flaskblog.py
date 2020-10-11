from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm 
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY']='3090657a7c7bbbfebf02f365802085fe'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db' #/// for relative location
db=SQLAlchemy(app)

class User(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(20),unique=True,nullable=False)
    email=db.Column(db.String(30),unique=True,nullable=False)
    image_file=db.Column(db.String(20),nullable=False,default='default.jpg')
    password=db.Column(db.String(60),nullable=False)
    posts=db.relationship('Post',backref='author',lazy=True)#one-to-many relationship , backref is similar to a column and author will give the user who created the post

    def __repr__(self):
    	return f"User('{self.username}','{self.email}','{self.image_file}')"

class Post(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(100),nullable=False)
    date_posted=db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    content=db.Column(db.Text,nullable=False)
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False) #foreign Key for Class=User===table=user
    def __repr__(self):
        return f"Post('{self.title}','{self.date_posted}')"

		
	

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
    form=RegistrationForm()
    if form.validate_on_submit():
    	flash(f'Account created for {form.username.data}!', 'success')
    	return redirect(url_for('home'))
    return render_template('register.html',title='Register', form=form)
    
@app.route('/login',methods=['GET','POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
    	if form.email.data=='admin@blog.com' and form.password.data=='password':
    		flash('Successfully logged in!','success')
    	else:
    		flash('Not logged in. Check username and password','danger') #danger bootstrap class will pop texk as color red
    return render_template('login.html',title='Login', form=form)
if __name__ == '__main__':
	app.run(debug=True)
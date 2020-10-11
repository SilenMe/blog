from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm 

app = Flask(__name__)
app.config['SECRET_KEY']='3090657a7c7bbbfebf02f365802085fe'


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
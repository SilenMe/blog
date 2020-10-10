from flask import Flask, render_template, url_for 

app = Flask(__name__)

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
def hello():
    return render_template('home.html',posts=posts) #posts=posts tell that, we can use 'posts' variale (which is defined here) as 'posts' in any templates

@app.route('/about')
def about():
    return render_template('about.html',title='About')

if __name__ == '__main__':
	app.run(debug=True)
from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
	user = {'nickname':'Owner'}
	posts = [
		{
		'author':{'nickname':'Bruce'},
		'body': 'This is my 1st post'
		},
		{
		'author':{'nickname':'Yang'},
		'body':'This is my 2nd post'
		}
	]
	return render_template("index.html",
		title = 'Home',
		user = user,
		posts = posts) 

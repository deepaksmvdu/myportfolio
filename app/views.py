from app import app
from flask import render_template,request,redirect,make_response
from forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')



@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if request.method == "POST":
		userData = form.data
		if userData["username"]=="deepak" and userData["password"]=="junmun":
			return redirect('/dashboard')
		else:
			return "NOT Authorize"
	else:
		return render_template('login.html', title='Sign In',form=form)



@app.route('/dashboard')
def dashboard():
	return make_response(render_template('dashboard.html'))
 
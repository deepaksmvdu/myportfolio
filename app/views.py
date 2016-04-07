from app import app
from flask import render_template,request,redirect,make_response,url_for,session
from forms import LoginForm
import json
import cloudinary
import cloudinary.uploader
import cloudinary.api
cloudinary.config( 
  cloud_name = "dvehlbgrc", 
  api_key = "553354936126149", 
  api_secret = "nFTx1NQOHqOIU42EOyW_0YEWYmc" 
)
@app.route('/')
@app.route('/index')
def index():
	session["username"] = "NotAuth"
	return render_template('index.html')



@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if request.method == "POST":
		userData = form.data
		if userData["username"]=="deepak" and userData["password"]=="junmun":
			session['username']='deepakjunmun'

			return redirect('/dashboard#/')
		else:
			return "NOT Authorize"
	else:
		return render_template('login.html', title='Sign In',form=form)



@app.route('/dashboard')
def dashboard():
	return make_response(render_template('dashboard.html'))
 

@app.route('/PicsList')
def test():
	print session
	if session["username"] == "deepakjunmun":
		imgUrl = []
		finalImg =[]
		result = cloudinary.api.resources(max_results=500)
		for r in range(len(result["resources"])):
			imgUrl.append(result["resources"][r]["secure_url"])


		# for r in range(len(imgUrl)):
		# 	x =  imgUrl[r].split("upload/")
		# 	finalImg.append(x[0]+"upload/"+"c_scale,h_1024,w_300/"+x[1])

		print imgUrl
		return json.dumps(imgUrl)
	else:
		return "Not Authorize"


	 
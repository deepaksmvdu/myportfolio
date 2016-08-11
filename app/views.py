from app import app
from flask import render_template,request,redirect,make_response,url_for,session
from flask_mysqldb import MySQL
from forms import LoginForm
import MySQLdb as db
import MySQLdb
import MySQLdb.cursors
import tweepy
import re
from urlparse import urlparse
import json
mysql = MySQL()
connection = db.connect(host='localhost', user='root',passwd ='root',db="twitterdb",cursorclass=MySQLdb.cursors.DictCursor)
cursor = connection.cursor()
consumer_key='IdrlU8eDhFRJT7ZNzLP6iAORt'
consumer_secret='LnrtgWseH5lMF6dRJfqLyTWPfO1lfPcAIxCB7lO6NENI6t5c4n'
access_token='1441805252-mL3LEQfPP5YzxQLVQerkj32GbecSflRITonh6pd'
access_token_secret='Wi61O68manrz9o9e9PI1qS9otn2sUQHApbJgo5F0SYJiS'


@app.route('/')
@app.route('/index')
def index():
	session["username"] = "NotAuth"
	return render_template('index.html')



def checkUnicode(stringval):
        if isinstance(stringval,basestring):
            return stringval.encode('utf8')
        else:
            return unicode(stringval).encode('utf8')
def HashTags(search_results):
    tweetDict = {}
    for tweet in search_results:
        docs = tweet._json
        if 'text' not in docs:
            tweetDict["text"] = "Unable to fetch Text"
        else:
            tweetDict["text"] = checkUnicode(docs["text"])

        if 'id' not in docs:
            tweetDict["id"] = 0
        else:
            tweetDict["id"] = docs["id"]

        if 'hashtags' not in docs["entities"]:
            tweetDict["hashtag"] = "Unable to fetch Text"
        else:
            hashtag = []
            for r in range(len(docs["entities"]["hashtags"])):
                hashtag.append(docs["entities"]["hashtags"][r]["text"])
            tweetDict["hashtag"] = str(hashtag)
            tweetDict['hashtag'] =re.sub("u'([^']*)'",r'\1',tweetDict['hashtag'])

        if "name" not in docs["user"]:
            tweetDict["name"] = "Unable to fetch Text"
        else:
            tweetDict["name"] = checkUnicode(docs["user"]["name"])

        if "profile_image_url_https" not in docs["user"]:
            tweetDict["userimage"] = "Unable to fetch Text"
        else:
            tweetDict["userimage"] = docs["user"]["profile_image_url_https"]
            tweetDict["userimage"] = str(tweetDict["userimage"])
            tweetDict['userimage'] =re.sub("u'([^']*)'",r'\1',tweetDict['userimage'])

        if "screen_name" not in docs["user"]:
            tweetDict["userimage"] = "Unable to fetch Text"
        else:
            tweetDict["screenName"] = docs["user"]["screen_name"]  
            tweetDict["screenName"] = str(tweetDict["screenName"])
            tweetDict['screenName'] =re.sub("u'([^']*)'",r'\1',tweetDict['screenName'])


        if "id" not in docs["user"]:
            tweetDict["userId"] = "Unable to fetch Text"
        else:
            tweetDict["userId"] = docs["user"]["id"]        

        
        cursor.execute('''INSERT into twitterTable(tweet,tweet_id,hashtags,media_url,user,username,user_id)values (%s,%s, %s,%s, %s,%s,%s)''',(tweetDict["text"],tweetDict["id"],tweetDict["hashtag"],tweetDict["userimage"],tweetDict["name"],tweetDict["screenName"],tweetDict["userId"]))
        connection.commit()

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if request.method == "POST":
		userData = form.data
		if userData["username"]=="deepak" and userData["password"]=="tracnx":
			session['username']='deepaktracnx'

			return redirect('/dashboard#/')
		else:
			return "NOT Authorize"
	else:
		return render_template('login.html', title='Sign In',form=form)



@app.route('/dashboard')
def dashboard():
	return make_response(render_template('dashboard.html'))
 

@app.route('/PicsList/<hashtag>')
def test(hashtag):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    search_results = api.search(q='#'+hashtag,count=1000)
    HashTags(search_results)
    cursor.execute('SELECT * FROM twitterTable ORDER BY id  DESC LIMIT 20')
    data = list(cursor.fetchall())
    return json.dumps({'data': data})






# Variables that contains the user credentials to access Twitter API 








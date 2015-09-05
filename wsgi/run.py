import os
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)
app.config['SERVER_NAME']="gorti.me"
#Create our index or root / route
@app.route("/")
def redirect():
    return "HOMEPAGE"
@app.route("/",subdomain="abhishek")
def index():
    content="Hello. <br>This is Abhishek Gorti's personal website. <br>There will definitely be more to come. <br>Please check back often. <br>More links will be in the menu(:hover) <br>-waco001 8/22/15"
    return render_template('index.html', contentraw=content)
@app.route("/about",subdomain="abhishek")
def about():
    content="About Me - Nothing Yet!"
    return render_template('index.html', contentraw=content)
@app.route("/blog",subdomain="abhishek")
def blog():
    content="No entries Yet!"
    return render_template('index.html', contentraw=content)
@app.route("/contact",subdomain="abhishek")
def contact():
	content="Call Me.<br>312.725.0351<br>Email Me<br>abhishek.gorti@gmail.com<br>skype:f18fan"
	return render_template('index.html', contentraw=content)
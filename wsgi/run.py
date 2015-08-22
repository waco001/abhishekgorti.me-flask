import os
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)
app.config['SERVER_NAME']="abhishek.gorti.me"
#Create our index or root / route
@app.route("/")
def index():
    content="Hello. <br>This is Abhishek Gorti's personal website. <br>There will definitely be more to come. <br>Please check back often. <br>More links will be in the menu(:hover) <br>-waco001 6/23/15 <br>If you need me, add me on skype:f18fan"
    return render_template('index.html', contentraw=content)
@app.route("/contact")
def contact():
	content="Call Me.<br>312.725.0351<br>Email Me<br>abhishek.gorti@gmail.com"
	return render_template('index.html', contentraw=content)
@app.route("/portfolio", subdomain='foo')
def portfolio():
	content="More Coming Soon"
	return render_template('index.html', contentraw=content)
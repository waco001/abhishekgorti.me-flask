import os
from flask import Flask
from flask import render_template
from flask import request
from abhishekgorti import abhishekgorti
app = Flask(__name__)
app.config['SERVER_NAME']="gorti.me"
app.register_blueprint(abhishekgorti)
#Create our index or root / route

@app.route("/",subdomain='www')
@app.route("/")
def index():
    content="Hello, you must be looking for Abhishek's Website: <a href='http://abhishek.gorti.me'>abhishek.gorti.me</a>"
    return content
from flask import render_template
from flask import request, Blueprint
abhishekgorti = Blueprint('abhishekgorti',__name__,subdomain='abhishek')

@abhishekgorti.route("/")
def index():
    content="Hello. <br>This is Abhishek Gorti's personal website. <br>There will definitely be more to come. <br>Please check back often. <br>More links will be in the menu(:hover) <br>-waco001 8/22/15"
    return render_template('index.html', contentraw=content)
@abhishekgorti.route("/about")
def about():
    content="About Me - Nothing Yet!"
    return render_template('index.html', contentraw=content)
@abhishekgorti.route("/blog")
def blog():
    content="No entries Yet!"
    return render_template('index.html', contentraw=content)
@abhishekgorti.route("/contact")
def contact():
    content="Call Me.<br>312.725.0351<br>Email Me<br>abhishek.gorti@gmail.com<br>skype:f18fan"
    return render_template('index.html', contentraw=content)
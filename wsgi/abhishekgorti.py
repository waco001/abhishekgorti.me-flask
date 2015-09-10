from flask import render_template
from flask import request, Blueprint
abhishekgorti = Blueprint('abhishekgorti',__name__,subdomain='abhishek')

@abhishekgorti.route("/")
def index():
    content="Hi!<br>My name is Abhishek Gorti. I am a student at Hamden High School.<br>A few things about me:<br><ul><li>I am addicted to programming</li><li>I love aviation and am a student pilot.</li><li>I need to know how everything works.</li></ul><br>You can navigate by hovering over the menu bar above.<br><a href='http://gorti.me/sitelist'>Sitelist</a>"
    return render_template('index.html', contentraw=content)
@abhishekgorti.route("/blog")
def blog():
    content="Timeline:<br>This is not my blog, but this is where I will post my programming projects.<br>The internet has a new form of art for people like me. I'll make cool works that will demonstrate my skill of design, function, and art.<br>I currently working on a project. It will be done around October. Check back then."
    return render_template('index.html', contentraw=content)
@abhishekgorti.route("/contact")
def contact():
    content="Call Me.<br>312.725.0351<br>Email Me<br>abhishek.gorti@gmail.com<br>skype:f18fan"
    return render_template('index.html', contentraw=content)

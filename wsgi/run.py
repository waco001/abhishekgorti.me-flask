import os
from flask import Flask
from flask import render_template, make_response
from flask import request
from abhishekgorti import abhishekgorti
app = Flask(__name__)
app.register_blueprint(abhishekgorti)
PAGE_LAST_MODIFIED = '2015-09-06'
#app.config['SERVER_NAME']="gorti.me"
#Create our index or root / route

@app.route("/",subdomain='www')
@app.route("/")
def index():
    content="Hello, you must be looking for Abhishek's Website: <a href='http://abhishek.gorti.me'>abhishek.gorti.me</a>"
    return content
@app.route('/sitemap',methods=['GET'])
@app.route('/sitemap.xml',methods=['GET'])
def sitemap():
    """Generate sitemap.xml """
    pages = []
    # All pages registed with flask apps
    for rule in app.url_map.iter_rules():
        if not rule.rule in pages:
            if "GET" in rule.methods and len(rule.arguments) == 0:
                subdomain=''
                if rule.subdomain is '':
                    subdomain=''
                else:
                    subdomain = rule.subdomain + "."
                pages.append("http://" + subdomain + app.config['SERVER_NAME'] + rule.rule)
    sitemap_xml = render_template('sitemap.xml', pages=pages,lm = PAGE_LAST_MODIFIED)
    response = make_response(sitemap_xml)
    response.headers["Content-Type"] = "application/xml"
    return response
if __name__ == '__main__':
    app.run(debug=True)
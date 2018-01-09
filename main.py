from flask import Flask, request
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def user_signup():
    template = jinja_env.get_template('usersignup.html')
    return template.render()

@app.route("/", methods=['POST'])
def welcome():
    username = request.form['username']
    template = jinja_env.get_template('welcome_page.html')
    return template.render(username=username)

app.run()
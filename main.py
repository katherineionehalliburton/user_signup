from flask import Flask, request
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def user_signup():
    template = jinja_env.get_template('usersignup.html')
    return template.render(Username_error = '', username = '', Password_error = '', password = '', Confirm_pass_error = '', confirm_pass = '', Email_error = '', email = '')

@app.route("/", methods=['POST'])
def validate_form():
    username = request.form['username']
    password = request.form['password']
    confirm_pass = request.form['confirm_pass']
    email = request.form['email']

    Username_error = ''
    Password_error = ''
    Confirm_pass_error = ''
    Email_error = ''

    if len(username) < 3 or len(username) > 20 or " " in username or username == "":
        Username_error = "Your entry must be between 3 and 20 characters and contain no spaces. Required field."
    if len(password) < 3 or len(password) > 20 or " " in password or password == "":
        Password_error = "Your entry must be between 3 and 20 characters and contain no spaces. Required field."
    if len(confirm_pass) < 3 or len(confirm_pass) > 20 or " " in confirm_pass or confirm_pass == "":
        Confirm_pass_error = "Your entry must be between 3 and 20 characters and contain no spaces. Required field."
        
    if email:
        if "." not in email and "@" not in email:
            Email_error = "Please check and re-submit. Please do not use spaces."

    if password != confirm_pass:
        Password_error = "Password and Confirm Password fields must match."
        Confirm_pass_error = "Password and Confirm Password fields must match."

    if not Username_error and not Password_error and not Confirm_pass_error and not Email_error:
        username = request.form['username']
        template = jinja_env.get_template('welcome_page.html')
        return template.render(username=username)
         
    else:
        template = jinja_env.get_template('usersignup.html')
        return template.render(username=username, Username_error=Username_error, password='',Password_error=Password_error, confirm_pass='', Confirm_pass_error=Confirm_pass_error, email=email, Email_error=Email_error)

app.run()
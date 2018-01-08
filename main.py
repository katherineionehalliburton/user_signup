from flask import Flask, request

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE HTML>
<html>
    <body>
        <form action="/" Method='POST'>
            
            <p><label for=username>Enter Username:</label>
            <input id="username" type=text name="username:"></p>

            <p><label for=password>Please enter password:</label>
            <input id="password" type=password name="password"></p>

            <p><label for=confirm_pass>Confirm Password:</label>
            <input id="confirm_pass" type=password name="confirm_pass"></p>

            <label for=email>Email:</label>
            <input id="email" type=text name="email">            
            <label for=checkbox>Select to receive email updates</label>
            <input id="checkbox" type=checkbox name="checkbox"> 

            <p><input id="submit" type=submit name="submit"></p>
        
        </form>
    </body>
</html>
"""
@app.route("/")
def input_rules():
    return form

@app.route("/WelcomePage", methods=['POST'])
def welcome():
    username = request.form['username']
    return '<h1>Welcome, ' + username + '</h1>'
app.run()
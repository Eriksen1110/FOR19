import flask 
from flask import request, flash 
import random

application = flask.Flask(__name__)

application.secret_key = "80e49e4bea0c03d64cc40d37f11535b85e93880b43c8c053"
DEV_PORT = 5000
PRO_PORT = 80

DEV_HOST = "localhost"
PRO_HOST = "0.0.0.0"

#mode = "production"
mode = "development"

@application.route("/", methods=['POST', 'GET'])
def home():
    names = ['Christian', 'Richard', 'Sara', "Carl-Oscar", "Jon", 'Vilde', "Martin"]
    name = names[round(random.randint(0,6))]
    return flask.render_template('home.html', name=name)

@application.route("/methodology")
def methodology():
    return flask.render_template("methodology.html")

@application.route("/carbon_app", methods=['POST', 'GET'])
def carbon_application():
    return flask.render_template("carbon_app.html")

@application.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        data = request.form
        print(f"Username: {data['email']}")
        print(f"Username: {data['password']}")
        flash("Congratz, you have successed to login")
        return flask.redirect("/")
    return flask.render_template('login.html')

@application.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        data = request.form
        print(f"First Name: {data['f:name']}")
        print(f"Last Name: {data['l:name']}")
        print(f"Email: {data['email']}")
        print(f"Password: {data['password']}")

    return flask.render_template('register.html')



@application.errorhandler(404)
def error(e):
    return flask.render_template('404.html') 

if __name__ == "__main__":
    if mode == "production":
        application.run(port=PRO_HOST, host=DEV_HOST)
    else:
        application.run(port=DEV_PORT, host=DEV_HOST, debug=True)

import flask 

app = flask.Flask(__name__)

DEV_PORT = 5000
PRO_PORT = 80

DEV_HOST = "localhost"
PRO_HOST = "0.0.0.0"

#mode = "production"
mode = "development"

@app.route("/", methods=['POST', 'GET'])
def home():
    return flask.render_template('home.html', name='Christian')

@app.route("/methodology")
def methodology():
    return flask.render_template("methodology.html")


@app.errorhandler(404)
def error(e):
    return flask.render_template('404.html') 

if __name__ == "__main__":
    if mode == "production":
        app.run(port=PRO_HOST, host=DEV_HOST, debug=True)
    else:
        app.run(port=DEV_PORT, host=DEV_HOST, debug=True)

import flask


app = flask.Flask(__name__)

@app.route('/')
def root():
    return flask.redirect("/s/index.html", code=302)

@app.route('/login')
def login():
    return flask.render_template("/s/login.html")

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
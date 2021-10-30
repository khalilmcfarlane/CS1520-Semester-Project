import flask
import user
from google.cloud import datastore
from flask import flash, redirect, render_template, request, url_for
um = user.User_manager()

app = flask.Flask(__name__)
app.secret_key = "jdofewpjofawiejf"
client = datastore.Client()


@app.route('/')
def root():
    return flask.redirect("/s/index.html", code=302)

@app.route('/send', methods=['POST','GET'])
def register_user():
    username = flask.request.form['username']
    password = flask.request.form['password']
    um.register(username, password) # register the new user
    print("registered username", username)
    return flask.render_template("profile.html", username = username)

@app.route('/login', methods=['POST','GET'])
def login():
    username = flask.request.form['username']
    password = flask.request.form['password']
    response = um.login(username, password) # register the new user
    print(response)
    if response == "User Not Found" or response == "Wrong Password":
        print("yo")
        error = "User Not Found"
        return flask.render_template('error.html', error=error)
    return flask.render_template("profile.html", username = username)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)

import flask
import user
import post
from google.cloud import datastore
from flask import flash, redirect, render_template, request, url_for
from forms_manager import *
um = user.User_manager()
post = post.PostsManager()

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
    age = flask.request.form['age']
    city = flask.request.form['city']
    major = flask.request.form['major']
    school = flask.request.form['school']
    um.register(username, password, age, city, major, school) # register the new user
    print("registered username", username)
    return flask.render_template("profile.html", username = username, age = age, city = city, major = major, school = school)

@app.route('/login', methods=['POST','GET'])
def login():
    username = flask.request.form['username']
    password = flask.request.form['password']
    response = um.login(username, password) # register the new user
    print(response)
    if response == "User Not Found" or response == "Wrong Password":
        error = "User Not Found"
        return flask.render_template('error.html', error=error)
    age = response['age'] 
    city = response['city'] 
    major = response['major'] 
    school = response['school']
    return flask.render_template("profile.html", username = username, age = age, city = city, major = major, school = school)

@app.route('/create', methods=['GET', 'POST'])
def create_post():
    form = NewPostForm(flask.request.form)
    if flask.request.method == 'POST':
        title = form.title.data
        article = form.article.data

        #if title and article:
        post.store_post(title, article)
        return redirect('/post', title)
    
    return flask.render_template("createpost.html", form=form)


@app.route('/post')
def display_post(title):
    message = post.find_post(title)
    return render_template('create-post.html', title=message.title, article=message.article)



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)

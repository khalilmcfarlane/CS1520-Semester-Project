import flask
import user
import post
from google.cloud import datastore
from flask import flash, redirect, render_template, request, url_for
um = user.User_manager()
post = post.PostsManager()

app = flask.Flask(__name__)
app.secret_key = "jdofewpjofawiejf"
client = datastore.Client()


@app.route('/')
def root():
    return flask.redirect("/s/main.html", code=302)

@app.route('/send', methods=['POST','GET'])
def register_user():
    username = flask.request.form['username']
    password = flask.request.form['password']
    age = flask.request.form['age']
    city = flask.request.form['city']
    major = flask.request.form['major']
    school = flask.request.form['school']
    um.register(username, password, age, city, major, school) # register the new user
    post.store_user(username)
    print("registered username", username)
    return flask.render_template("profile.html", username=username, age=age, city=city, major=major, school=school)

@app.route('/login', methods=['POST','GET'])
def login():
    username = flask.request.form['username']
    password = flask.request.form['password']
    is_logged = True
    response = um.login(username, password) # register the new user
    print(response)
    if response == "User Not Found" or response == "Wrong Password":
        error = "User Not Found"
        return flask.render_template('error.html', error=error)
    age = response['age'] 
    city = response['city'] 
    major = response['major'] 
    school = response['school']
    messages = post.query_post_by_username(username)
    return flask.render_template("login-profile.html", username=username, age=age, city=city, major=major, school=school, is_logged=is_logged, messages=messages)

@app.route('/create', methods=['GET', 'POST'])
def create_post():
    if flask.request.method == 'POST':
        title = flask.request.form['title']
        article = flask.request.form['article']
        post.store_post(title, article)
        return redirect('/post/%s/' % (title))
    
    return flask.render_template("createpost.html")


@app.route('/post/<title>/')
def display_post(title):
    message = post.query_post_by_title(title)
    title = message['title']
    article = message['article']
    return render_template('post.html', title=title, article=article)

@app.route('/profile/posts/')
def display_user_posts(username):
    message = post.query_post_by_username(username)
    username = message['username']
    title = message['title']
    article = message['article']
    return render_template('userposts.html', username=username, title=title, article=article)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)

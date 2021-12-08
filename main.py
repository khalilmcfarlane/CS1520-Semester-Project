import flask
import user
import post
from google.cloud import datastore
from flask import flash, redirect, render_template, request, url_for, session
um = user.User_manager()
post = post.PostsManager()
app = flask.Flask(__name__)
app.secret_key = "jdofewpjofawiejf"
client = datastore.Client()

class Username():
    def __init__(self):
        self.username = "Anonymous"
    def update_username(self, user):
        self.username = user

    def return_username(self):
        return self.username

current_user = Username()

@app.route('/')
def root():
    posts = post.return_posts()

    if len(posts) == 0:
        return flask.redirect("/")
    return flask.render_template("main.html", posts=posts)

@app.route('/sports')
def filter_by_sports(tag):
    posts = post.return_posts()
    posts_filtered = [] 
    for post in posts:
        if post['tag'] == "sports":
            posts_filtered.append(post)
    return flask.render_template("tag-posts.html", posts=posts_filtered)

@app.route('/news')
def filter_by_news(tag):
    posts = post.return_posts()
    posts_filtered = [] 
    for post in posts:
        if post['tag'] == "news":
            posts_filtered.append(post)
    return flask.render_template("tag-posts.html", posts=posts_filtered)

@app.route('/media')
def filter_by_media(tag):
    posts = post.return_posts()
    posts_filtered = [] 
    for post in posts:
        if post['tag'] == "media":
            posts_filtered.append(post)
    return flask.render_template("tag-posts.html", posts=posts_filtered)

@app.route('/school')
def filter_by_school(tag):
    posts = post.return_posts()
    posts_filtered = [] 
    for post in posts:
        if post['tag'] == "school":
            posts_filtered.append(post)
    return flask.render_template("tag-posts.html", posts = posts_filtered)

@app.route('/food')
def filter_by_food(tag):
    posts = post.return_posts()
    posts_filtered = [] 
    for post in posts:
        if post['tag'] == "food":
            posts_filtered.append(post)
    return flask.render_template("tag-posts.html", posts=posts_filtered)

@app.route('/other')
def filter_by_other(tag):
    posts = post.return_posts()
    posts_filtered = [] 
    for post in posts:
        if post['tag'] == "other":
            posts_filtered.append(post)
    return flask.render_template("tag-posts.html", posts=posts_filtered)





@app.route('/send', methods=['POST','GET'])
def register_user():
    username = flask.request.form['username']
    current_user.update_username(username)
    password = flask.request.form['password']
    age = flask.request.form['age']
    city = flask.request.form['city']
    major = flask.request.form['major']
    school = flask.request.form['school']
    session['username'] = username

    um.register(username, password, age, city, major, school) # register the new user
    # post.store_user(username)
    print("registered username", username)
    return flask.render_template("login-profile.html", username=username, age=age, city=city, major=major, school=school)

@app.route('/login', methods=['POST','GET'])
def login():
    username = flask.request.form['username']
    current_user.update_username(username)
    password = flask.request.form['password']

    response = um.login(username, password) # register the new user
    if response == "User Not Found" or response == "Wrong Password":
        #error = "User Not Found"
        return redirect('/s/login.html')
    session['username'] = username
    age = response['age'] 
    city = response['city'] 
    major = response['major'] 
    school = response['school']
    is_logged = True
    messages = post.query_post_by_username(username)
    return flask.render_template("login-profile.html", username=username, age=age, city=city, major=major, school=school, is_logged=is_logged, messages=messages)

@app.route('/create', methods=['GET', 'POST'])
def create_post():
    if request.method == 'POST':
    #     title = flask.request.form['title']
    #     article = flask.request.form['article']
    #     name = current_user.return_username()
    #     print("This is the name mateeeeee" , name)
    #     post.store_post(title, article, name)
    #     post.return_posts()
    #     return redirect('/post/%s' %title)
    
        if 'username' in session:
            username = session['username']
            title = flask.request.form['title']
            article = flask.request.form['article']
            tag = flask.request.form['tag']
            post.store_post(title, article, username, tag)
            return redirect('/posts/%s/%s/' % (username, title))
        else:
            return redirect('/s/login.html')
    return flask.render_template("createpost.html")


@app.route('/posts/<username>/<title>/')
def display_post(username, title):
    message = post.query_post_by_title(title)
    title = message['title']
    article = message['article']
    return render_template('post.html', title=title, article=article)

#class Username():
 #   def __init__(self):
  #      self.username = "Guadalupe"
   # def update_username(self, user):
    #    self.username = user

   # def return_username(self):
    #    return self.username

@app.route('/profile/posts/')
def display_user_posts(username):
    message = post.query_post_by_username(username)
    return render_template('userposts.html', message=message)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)

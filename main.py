import flask
from flask import url_for
from google.cloud import datastore

app = flask.Flask(__name__)
client = datastore.Client()

'''
    Stores username/password via flask in cloud datastore.
    More reliable than JS, which is easy to change the source code.
    Will use in signup()
'''
def store_entity():
    pass
'''
    Retrieves stored entity.
    Useful in testing in user verification during login
'''
def fetch_entity():
    pass

@app.route('/')
def root():
    return flask.redirect("/s/index.html", code=302)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if "username" in flask.session:
        pass
        #return flask.redirect(url_for("Profile", username=flask.session["username"]))
    elif flask.request.method == "POST":
        if flask.request.form["user"] in entity:
            pass
            # Find entity key (password)
            #return redirect to profile
    return flask.render_template("/s/login.html")

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    return flask.render_template("/s/signup.html")

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
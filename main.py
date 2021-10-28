import flask
from flask import url_for
from flask.globals import request
from google.cloud import datastore

app = flask.Flask(__name__)
client = datastore.Client()

'''
    Stores username/password via flask in cloud datastore.
    More reliable than JS, which is easy to change the source code.
    Will use in signup()
'''
def store_entity(username, password):
    key = client.key('User', username)
    entity = datastore.Entity(key=key)
    entity.update({
        username: password,
    })
    client.put(entity)


'''
    Retrieves stored entity.
    Useful in testing in user verification during login
'''
def fetch_entity():
    query=client.query(kind='User')
    results = list(query)
    return results

@app.route('/')
def root():
    return flask.redirect("/s/index.html", code=302)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if "username" in flask.session:
        pass
        #return flask.redirect(url_for("Profile", username=flask.session["username"]))
    elif flask.request.method == "POST":
        results = fetch_entity()
        if flask.request.form["username"] in results:
            for elem in results:
                if elem == flask.request.form["username"]: 
                    return flask.redirect(url_for("root", username=flask.session["username"]))
            # Find entity key (password)
            #return redirect to profile
    return flask.render_template("/s/login.html")

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if flask.request.method == "POST":
        store_entity(flask.request.form["username"], flask.request.form["password"])        
    return flask.render_template("/s/signup.html")

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
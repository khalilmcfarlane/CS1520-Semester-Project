import flask
from google.cloud import datastore

app = flask.Flask(__name__)
client = datastore.Client()


@app.route('/')
def root():
    return flask.redirect("/s/index.html", code=302)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
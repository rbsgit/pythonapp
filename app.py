import os

import flask

app = flask.Flask(__name__)


@app.route("/")
def hello():
    return "Hello world, Python in PAAS"

app.run(port=int(os.environ.get("PORT", "5000")), host="0.0.0.0")

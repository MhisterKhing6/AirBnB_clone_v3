#!/usr/bin/python3
"""
The start of my api
"""
from api.v1.views import app_views
from flask import Flask, jsonify
from models import storage
from os import getenv

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def clos(self):
    """
    close the storage after an operation
    """
    storage.close()


@app.errorhandler(404)
def error(name):
    return jsonify({"error": "Not found"})


if __name__ == "__main__":
    host = "0.0.0.0"
    port = "5000"
    if getenv("HBNB_API_HOST"):
        host = getenv("HBNB_API_HOST")
    if getenv("HBNB_API_PORT"):
        port = getenv("HBNB_API_PORT")
    app.run(host=host, port=port, threaded=True)

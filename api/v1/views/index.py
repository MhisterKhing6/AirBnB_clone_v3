#!/usr/bin/python3
"""
Create a route
"""
from api.v1.views import app_views
from flask import jsonify


@app_views.route("/status")
def status():
    """
    Return a json object
    """
    obj = {"status": "ok"}
    return jsonify(obj)

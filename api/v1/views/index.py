#!/usr/bin/python3
"""
Create a route
"""
from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


@app_views.route("/status")
def status():
    """
    Return a json object
    """
    obj = {"status": "ok"}
    return jsonify(obj)


@app_views.route("/stats")
def stats():
    t = {key: storage.count(value) for key, value in classes.items()}
    return jsonify(t)

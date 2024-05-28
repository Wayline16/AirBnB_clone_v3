#!/usr/bin/python3
'''Contains the places view for the API.'''
from flask import abort, jsonify, make_response, request
from api.v1.views import app_views
from models import storage
from models.place import Place


@app_views.route('/places', methods=['GET'], strict_slashes=False)
def places():
    """Retrieves the list of all User objects"""
    objs = storage.all(Place)
    return jsonify([obj.to_dict() for obj in objs.values()])
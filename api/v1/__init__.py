#!/usr/bin/python3
"""
Create a new Flask app blueprint
"""
from flask import Blueprint

app_views = Blueprint('app_viws', __name__, url_prefix= '/api/v1')


from api.v1.views.index import *
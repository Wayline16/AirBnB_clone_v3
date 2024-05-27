#!/usr/bin/python3
"""
Create a new Flask app, app_views
"""
from flask import jsonify
from api.v1.views import app_views

@app_views.route('/status')
def api_status():
    """
    what what
    """
    response =  {'status': "OK"}
    return jsonify(response)

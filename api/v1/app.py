#!/usr/bin/python3
"""Create a new Flask app, register blueprint app_views toFlask instance
"""
from os import getenv
from flask import Flask
from models import storage
from api.v1.views import app_views
from flask import jsonify

app = Flask(__name__)

app.register_blueprint(app_views)

@app.teardown.appcontext
def teardown_engine(exception):
    """
    close storage
    """
    storage.close()

@app.errorhandler(404)
def not_found(error):
    """
    Page not found
    """
    response = {"error": "Not found"}
    return jsonify(response), 404

if __name__ == '__main__':
    HOST = getenv('HBNB_API_HOST', '0.0.0.0')
    PORT = int(getenv('HBNB_API_HOST', 5000))
    app.run(debug=True, host=HOST, port=PORT, threaded=True)
    
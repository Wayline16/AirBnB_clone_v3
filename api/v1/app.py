#!/usr/bin/python3
'''Create a new Flask app
'''
from os import getenv
from flask import Flask
from models import storage
from api.v1.views import app_views
from flask import jsonify

app = Flask(__name__)

app.register_blueprint(app_views)
app.url_map.strict_slashes = False


@app.teardown.appcontext
def teardown_engine(exception):
    """close storage
    """
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """Page not found
    """
    response = {"error": "Not found"}
    return jsonify(response), 404


if __name__ == "__main__":
    host = getenv('HBNB_API_HOST')
    port = getenv('HBNB_API_PORT')
    if not host:
        host = '0.0.0.0'
    if not port:
        port = '5000'
    app.run(host=host, port=port, threaded=True)

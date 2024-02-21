#!/usr/bin/python3
"""A script that starts a Flask web Application."""
from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """Prints Hello HBNB! when / is called"""
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')

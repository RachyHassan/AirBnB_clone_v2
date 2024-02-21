#!/usr/bin/python3
"""A script that starts a web application
Requirements:
    -web application must be listening on 0.0.0.0, port 5000
    -Routes: /- displays "Hello HBNB"
    /hbnb: displays "HBNB"
"""
from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    """A function that prints Hello HBNB! when called"""
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """A function that prints HBNB when called"""
    return "HBNB"


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0', debug=True)

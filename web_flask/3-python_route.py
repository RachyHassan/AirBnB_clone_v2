#!/usr/bin/python3
"""A script that starts a Flask web application
Requirements:
    /: display “Hello HBNB!”
    /hbnb: display “HBNB”
    /c/<text>: display “C ”, followed by the value of the
    text variable (replace underscore _ symbols with a space )
    /python/<text>: display “Python ”, followed by the value
    of the text variable (replace underscore _ symbols with a space )
    The default value of text is “is cool”
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


@app.route('/c/<text>')
def c_is_fun(text):
    """A function that returns C is fun when called"""
    return 'C ' + text.replace("_", " ")


@app.route('/python/', defaults={'text': 'is cool'})
@app.route('/python/<text>')
def python_is_fun(text='is_cool'):
    """A function that returns Python is cool"""
    return 'Python ' + text.replace("_", " ")


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')

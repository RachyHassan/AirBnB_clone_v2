#!/usr/bin/python3
"""A script that starts a flask web Applicationk"""
from flask import Flask, abort


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    """A function that prints Hello HBNB!"""
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """A function that prints HBNB"""
    return "HBNB"


@app.route('/c/<text>')
def c_is_fun(text):
    """A function that returns C is fun"""
    return 'C ' + text.replace("_", " ")


@app.route('/python/', defaults={'text': 'is cool'})
@app.route('/python/<text>')
def python_is_fun(text='is_cool'):
    """A function that returns python is cool"""
    return 'Python ' + text.replace("_", " ")


@app.route('/number/<int:n>')
def number_n(n):
    """ A function that returns "n is a number". """
    return f'{n} is a number'


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')

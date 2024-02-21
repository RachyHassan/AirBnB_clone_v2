#!/usr/bin/python3
"""A script that starts a Flask web application:

    Your web application must be listening on 0.0.0.0, port 5000
    Routes:
        /: display “Hello HBNB!”
        /hbnb: display “HBNB”
        /c/<text>: display “C ”, followed by the value of
        the text variable (replace underscore _ symbols with a space )
        /python/(<text>): display “Python ”, followed by
        the value of the text variable (replace
        underscore _ symbols with a space )
        The default value of text is “is cool”
        /number/<n>: display “n is a number” only if n is an integer
        /number_template/<n>: display a HTML page only if n is an integer:
            H1 tag: “Number: n” inside the tag BODY
            /number_odd_or_even/<n>: display a HTML page
            only if n is an integer:
                H1 tag: “Number: n is even|odd” inside the tag BODY
"""
from flask import Flask, render_template


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
    """A function that returns Python is cool"""
    return 'Python ' + text.replace("_", " ")


@app.route('/number/<int:n>')
def number_n(n):
    """A function that returns n Is a number"""
    return f'{n} is a number'


@app.route('/number_template/<int:n>')
def number_template(n):
    """A function that retirns an HTML page if n is a number"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def odd_n_even(n):
    """A function that returns even|odd inside the tag BODY"""
    if n % 2 == 0:
        state = 'even'
    else:
        state = 'odd'
    return render_template('6-number_odd_or_even.html', n=n, state=state)


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')

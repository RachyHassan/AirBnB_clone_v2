#!/usr/bin/python3
""" A script that starts a Flask web application. 
Requirements:
    Your web application must be listening on 0.0.0.0, port 5000
    You must use storage for fetching data
    from the storage engine (FileStorage or DBStorage) =>
    from models import storage and storage.all(...)
    After each request you must remove the current SQLAlchemy Session:
    Declare a method to handle @app.teardown_appcontext
    Call in this method storage.close()
    Routes:
    /states_list: display a HTML page: (inside the tag BODY)
    H1 tag: “States”
    UL tag: with the list of all State objects present
    in DBStorage sorted by name (A->Z) tip
    LI tag: description of one State: <state.id>: <B><state.name></B>
    Import this 7-dump to have some data
"""
from flask import Flask
from flask import render_template
from models import *
from models import storage
app = Flask(__name__)
app.url_map.strictslashes = False


@app.route('/states_list')
def states_list():
    """ A function that displays a HTML page with
    states in alphabetical order. """
    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_page(exception):
    """ A function to close all storage on teardown. """
    storage.close()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5000')


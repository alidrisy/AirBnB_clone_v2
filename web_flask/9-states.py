#!/usr/bin/python3
""" Flask web application """

from flask import Flask, render_template
from models import *
from models import storage
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states(id=None):
    """Display a HTML page with list states or state and his cities """
    dict_states = storage.all("State")
    states = None
    name = None
    if id is not None:
        k = f"State.{id}"
        if k in dict_states:
            state = dict_states[k]
            name = state.name
            states = state.cities
    else:
        states = dict_states.values()
        name = None
    return render_template('9-states.html', states=states, name=name)


@app.teardown_appcontext
def teardown_db(exception):
    """ Remove the current SQLAlchemy Session """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')

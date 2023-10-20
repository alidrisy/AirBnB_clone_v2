#!/usr/bin/python3
""" Flask web application """
from flask import Flask, render_template
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/states_list")
def states_list():
    """ Display a HTML page with list of states """
    states = sorted(list(storage.all("State").values()), key=lambda s: s.name)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown(exc):
    """ Remove the current SQLAlchemy Session """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

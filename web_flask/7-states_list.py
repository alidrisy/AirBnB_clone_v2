#!/usr/bin/python3
""" Flask web application """
from flask import Flask, render_template
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def close(obj):
    """ Remove the current SQLAlchemy Session """
    storage.close()


@app.route('/states_list')
def states_list():
    """ Display a HTML page: (inside the tag BODY)
    H1 tag: “States”
    UL tag: with the list of all State objects present in DBStorage sorted
    by name (A->Z) tip
    LI tag: description of one State: <state.id>: <B><state.name></B> """
    states = list(storage.all('State').values())
    return render_template("7-states_list.html", states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

#!/usr/bin/python3
"""Minimal flask app"""

from flask import Flask, render_template
from models import storage
from models import State, Amenity
app = Flask(__name__)


@app.teardown_appcontext
def closedb(foo):
    """Closes db session"""
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """Route /hbnb_filters"""
    states = storage.all(State)
    amenities = storage.all(Amenity)
    return render_template('10-hbnb_filters.html', **locals())


if __name__ == '__main__':
    storage.reload()
    app.run("0.0.0.0", 5000)

#!/usr/bin/python3
"""starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states')
@app.route('/states/<id>')
def states_list(id=None):
    if id is None:
        id = '0'
    return render_template('9-states.html',
                           states=storage.all(State).values(), id=id)


@app.teardown_appcontext
def remove_session(exception):
    storage.close()

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)

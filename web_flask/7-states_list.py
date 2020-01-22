#!/usr/bin/python3
'''starts a Flask web application'''
from flask import Flask
from models import storage
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list')
def display_states():
    '''list all the states'''
    dict_states = storage.all("State")
    states = []
    for value in dict_states.values():
        states.append([value.id, value.name])
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown(exception):
    '''tear down db'''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

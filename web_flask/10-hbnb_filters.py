#!/usr/bin/python3
'''Flask web application '''
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/hbnb_filters')
def filters(id='0'):
    '''renders html content'''
    return render_template('10-hbnb_filters.html',
                           states=storage.all(State).values(),
                           amenities=storage.all(Amenity).values(),
                           id=id)


@app.teardown_appcontext
def teardown(exception):
    '''teardown db'''
    storage.close()


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)

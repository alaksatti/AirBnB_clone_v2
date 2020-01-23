c#!/usr/bin/python3
'''Flask web application '''
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/hbnb', strict_slashes=False)
def filters():
    '''renders html content'''
    return render_template('100-hbnb.html',
                           states=storage.all(State).values(),
                           amenities=storage.all(Amenity).values(),
                           places=storage.all(Place).values())


@app.teardown_appcontext
def teardown(exception):
    '''teardown db'''
    storage.close()


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)

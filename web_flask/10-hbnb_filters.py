#!/usr/bin/python3
'''starts a Flask web application '''
from flask import Flask, render_template
from models import storage
app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/hbnb_filters')
def filters():
    states = [[v.id, v.name] for v in storage.all("State").values()]
    cities = {}
    for v in storage.all("City").values():
        if v.state_id in cities.keys():
            cities[v.state_id].append(v.name)
        else:
            cities[v.state_id] = [v.name]
    amenities = [v.name for v in storage.all("Amenity").values()]
    return render_template('10-hbnb_filters.html',
                           states=states,
                           cities=cities,
                           amenities=amenities)


@app.teardown_appcontext
def teardown(exception):
    storage.close()


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)

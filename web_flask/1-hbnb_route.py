#!/usr/bin/python3
'  script that starts a Flask web application '
from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def HelloHNNB():
    return "Hello HBNB!"


@app.route('/hbnb')
def HBNB():
    return "HBNB"
if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)

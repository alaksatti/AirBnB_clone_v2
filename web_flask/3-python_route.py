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


@app.route('/c/<text>')
def C_text(text):
    return "C " + text.replace('_', ' ')


@app.route('/python/<text>')
@app.route('/python/')
def python_text(text=None):
    if text is None:
        text = "is cool"
    return "Python " + text.replace('_', ' ')

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)

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
def python_text(text="is cool"):
    return "Python " + text.replace('_', ' ')


@app.route('/number/<int:n>')
def n_integer(n):
    return str(n) + " is a number"


@app.route('/number_template/<int:n>')
def display_html(n):
    from flask import render_template
    return render_template('5-number.html', n=n)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)

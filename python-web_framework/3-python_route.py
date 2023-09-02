#!/usr/bin/python3
"""
Your web application must be listening on 0.0.0.0, port 5000
Routes:
/: Hello
/hbnb:
/c/<text>: , followed by the value of the text variable
(replace underscore _ symbols with a space)
/python/(<text>): , followed by the value of the text variable
(replace underscore _ symbols with a space)
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """ Display the site index """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    return "C " + text.replace("_", " ")


@app.route('/python/')
@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    return "Python " + text.replace("_", " ")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
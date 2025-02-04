#!/usr/bin/python3
''' starts a Flask web application
with host "0.0.0.0" and port "5000"
'''

from flask import Flask

app = Flask("__name__")


@app.route("/", strict_slashes=False)
def greet():
    ''' Greets Hello HBNB! on /'''
    return ("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    '''Displays hbnb on route /hbnb'''
    return ("HBNB")


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    '''Displays C with input "text" on /c/text'''
    return "C {}".format(text.replace("_", " "))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text="is cool"):
    '''Displays Python with "text" on /python/text'''
    return "Python {}".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)

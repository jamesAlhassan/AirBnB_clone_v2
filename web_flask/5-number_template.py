#!/usr/bin/python3
''' starts a Flask web application
with host "0.0.0.0" and port "5000"
'''

from flask import Flask, render_template

app = Flask("__name__")
app.url_map.strict_slashes = False

@app.route("/")
def greet():
    ''' Greets Hello HBNB! on /'''
    return ("Hello HBNB!")


@app.route("/hbnb")
def hbnb():
    '''Displays hbnb on route /hbnb'''
    return ("HBNB")


@app.route("/c/<text>")
def c_text(text):
    '''Displays C with input "text" on /c/text'''
    return "C {}".format(text.replace("_", " "))


@app.route("/python")
@app.route("/python/<text>")
def python_text(text="is cool"):
    '''Displays Python with "text" on /python/text'''
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>")
def isNum(n):
    '''Displays "n" is a number if n is an int passed on /number/n'''
    if isinstance(n, int):
        return "{} is a number".format(n)


@app.route("/number_template/<int:n>")
def numTemplate(n=None):
    '''Renders template "5-number.html" if n is an int'''
    if isinstance(n, int):
        return render_template("5-number.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

#!/usr/bin/python3
'''starts a Flask web application
with host "0.0.0.0" and port "5000"
'''
from flask import Flask, render_template


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def greet():
    ''' Greets Hello HBNB! on /'''
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """displays HBNB on /hbnb"""
    return "HBNB"


@app.route("/c/<text>")
def c_text(text):
    """Displays "C" followed by the value of text on /c/text"""
    return "C {}".format(text.replace("_", " "))


@app.route("/python")
@app.route("/python/<text>")
def python_text(text="is cool"):
    """
    Displays 'Python followed by the value of text variable
    Default value of text is 'is cool'
    """
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>")
def display_n(n):
    """Displays 'n is a number' only if n is an integer"""
    if isinstance(n, int):
        return "{} is a number".format(n)


@app.route("/number_template/<int:n>")
def display_html(n=None):
    """Renders a HTML page only if n is an integer"""
    if isinstance(n, int):
        return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>")
def display_even_odd(n=None):
    """Renders a HTML page only if n is an integer"""
    if isinstance(n, int):
        if (n % 2 == 0):
            return render_template("6-number_odd_or_even.html",
                                   n=n, text="even")
        else:
            return render_template("6-number_odd_or_even.html",
                                   n=n, text="odd")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

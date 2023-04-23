#!/usr/bin/python3
''' starts a Flask web application
with host "0.0.0.0" and port "5000" on with route "/"
'''

from flask import Flask

app = Flask("__name__")


@app.route("/", strict_slashes=False)
def greet():
    ''' Greets Hello HBNB! on /'''
    return ("Hello HBNB!")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)

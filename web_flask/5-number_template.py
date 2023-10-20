#!/usr/bin/python3
""" Flask web application """
from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    """ Display hello massige! """
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """ Display “HBNB” """
    return "HBNB"


@app.route('/c/<str1>')
def c_is(str1):
    """ Display “C ” followed by the value of the text variable
    (replace underscore _ symbols with) """
    return "C {}".format(str1.replace('_', ' '))


@app.route('/python/', defaults={'text': "is cool"})
@app.route('/python/<text>')
def python_is(text):
    """ Display “Python ”, followed by the value of the text variable
    (replace underscore _ symbols with a space ) """
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<int:n>')
def number(n):
    """ Display “n is a number” only if n is an integer """
    return f"{n} is a number"


@app.route('/number_template/<int:n>')
def number_template(n):
    """ Display a HTML page only if n is an integer:
    H1 tag: “Number: n” inside the tag BODY """
    return render_template('5-number.html', number=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

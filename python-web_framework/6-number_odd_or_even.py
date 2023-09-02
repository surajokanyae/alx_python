from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
def c(text):
    return "C " + text.replace("_", " ")

@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    return "Python " + text.replace("_", " ")

@app.route("/number/<n>", strict_slashes=False)
def number(n):
    if isinstance(n, int):
        return "n is a number"
    else:
        return "n is not a number"

@app.route("/number_template/<n>", strict_slashes=False)
def number_template(n):
    if isinstance(n, int):
        return render_template("number.html", n=n)
    else:
        return "n is not a number"

@app.route("/number_odd_or_even/<n>", strict_slashes=False)
def number_odd_or_even(n):
    if isinstance(n, int):
        return render_template("odd_or_even.html", n=n)
    else:
        return "n is not a number"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

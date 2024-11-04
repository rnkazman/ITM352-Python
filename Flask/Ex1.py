# First Flask example
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
@app.route("/")

def index():
    return("Welcome to a very boring web site!")


# Run the application
if __name__ == '__main__':
    app.run(debug=True)
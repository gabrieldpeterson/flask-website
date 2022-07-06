from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def my_home():
    return render_template('index.html')


@app.route("/index.html")
def index():
    return render_template('index.html')


@app.route("/elements.html")
def elements():
    return render_template('elements.html')


@app.route("/generic.html")
def generic():
    return render_template('generic.html')

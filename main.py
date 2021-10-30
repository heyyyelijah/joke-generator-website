from flask import Flask, render_template, redirect, url_for, request, flash, abort
import requests

app = Flask(__name__)
url = "https://v2.jokeapi.dev/joke/"

def request_joke(joke_type):
    response = requests.get(f'{url}{joke_type}')
    r = response.json()
    return r

@app.route('/')
def home():
    return render_template("index.html", home_page=True)

@app.route('/get_joke/pun', methods=["GET", "POST"])
def pun_joke():
    r = request_joke('Pun')
    return render_template("index.html", r=r)

@app.route('/get_joke/dark', methods=["GET", "POST"])
def dark_joke():
    r = request_joke('Dark')
    return render_template("index.html", r=r)

@app.route('/get_joke/xmas', methods=["GET", "POST"])
def xmas_joke():
    r = request_joke('Christmas')
    return render_template("index.html", r=r)

@app.route('/get_joke/any', methods=["GET", "POST"])
def any_joke():
    r = request_joke('Any')
    return render_template("index.html", r=r)

@app.route('/get_joke/spooky', methods=["GET", "POST"])
def spooky_joke():
    r = request_joke('Spooky')
    return render_template("index.html", r=r)

@app.route('/get_joke/programming', methods=["GET", "POST"])
def pc_joke():
    r = request_joke('Programming')
    return render_template("index.html", r=r)


if __name__ == "__main__":
    app.run(debug=True)
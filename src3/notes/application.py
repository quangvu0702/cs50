from flask import Flask, render_template, request

app = Flask(__name__)

notes = []

@app.route("/")
def index():
    return render_template("index_copy.html", notes=notes)

@app.route("/hello", methods=["POST"])
def hello():
    name = request.form.get('name')
    print(name)
    return render_template("more.html", name=name)
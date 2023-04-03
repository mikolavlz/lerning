import flask
from flask import render_template, request, jsonify

app = flask.Flask(__name__)

@app.route('/_add_numbers')
def add_numbers():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a + b)

@app.route("/")
def hello():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug = True)
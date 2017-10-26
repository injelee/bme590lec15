from flask import Flask, jsonify, request
app = Flask(__name__)


@app.route("/api/hello/<string:name>")
def helloworld(name):
    return "Hello World {}".format(name)


@app.route("/api/data/")
def jsondict():
    a = {"temp": [20, 21, 21]}
    b = {"time": [10, 20, 30]}
    c = {"unit": ["s"]}
    info = [a, b, c]
    return jsonify(info)


@app.route("/api/add/", methods=["Post"])
def jsonadd():
    ints = request.json
    tot = sum(ints.values())
    return "Sum was {}".format(tot)








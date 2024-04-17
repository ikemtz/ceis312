import tensorflow as tf
from flask import Flask, request
app = Flask(__name__)


@app.route("/")
def home():
    try:
        x = float(request.args.get('x'))
        print('x:', x)
        return "Yes"
    except ValueError:
        return "You must specifify the x querystring parameter with a number, example: '?x=5'", 400

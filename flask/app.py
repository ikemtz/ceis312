from flask import Flask, request
import pandas as pd
import tensorflow as tf
app = Flask(__name__)

model = tf.keras.models.load_model('2x1.keras')
columnArray = ['x']


@app.route("/")
def home():
    try:
        x = int(request.args.get('x'))
    except TypeError:
        return "You must specifify the 'x' querystring parameter, example: '?x=5'", 400
    except ValueError:
        return "The 'x' querystring parameter must have a numerical value, example: '?x=5'", 400

    simple_list = [x]
    simple_data = pd.DataFrame(simple_list, columns=columnArray)

    result_set = model.predict(simple_data)
    estimated_result = float(result_set[0][0])
    result = {
        'estimated': estimated_result,
        'actual': 2*x+1,
        'rounded(1):': round(estimated_result, 1),
        'rounded(0):': round(estimated_result, 0), }

    return result

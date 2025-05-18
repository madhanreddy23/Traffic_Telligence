import numpy as np
import os
import pickle
import pandas
from flask import Flask, request, jsonify, render_template

app = Flask(__name__, template_folder = 'templates')
model = pickle.load(open(r'C:\Users\surya\model.pk1', 'rb'))
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods = ["POST","GET"])
def predict():
    input_feature = [float(x) for x in request.form.values()]
    features_values = [np.array(input_feature)]
    names = [['holiday', 'temp', 'rain', 'snow', 'weather','year','month','day', 'hours', 'minutes', 'seconds']]
    data = pandas.DataFrame(features_values, columns= names)
    prediction = model.predict(data)
    print(prediction)
    text = "Estimated Traffic is: "
    return render_template('output.html', result = text+str(prediction)+'units')

if __name__ == "__main__" :
    port = int(os.environ.get('PORT',5000))
    app.run(port=port, debug=True, use_reloader=False)
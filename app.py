# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 20:30:22 2020

@author: Jeffin
"""

print("LErn Basic1111111111")
import numpy as np
from flask import Flask, request,  render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('spmodel.pkl', 'rb'))
print("LErn Basic222222221")
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='Employee Salary should be $ {}'.format(output))


if __name__ == "__main__":
    app.run(host = '0.0.0.0',debug=True, use_reloader=False)

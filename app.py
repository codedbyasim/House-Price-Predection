# app.py
from flask import Flask, render_template, request
import numpy as np
import pickle
import traceback

app = Flask(__name__)

# Load the trained model and scaler
model = pickle.load(open("linear_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))
poly = pickle.load(open("poly.pkl", "rb"))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict')
def predict():
    return render_template('predict.html')

@app.route('/result', methods=['POST'])
def result():
    try:
        # Get input values from form
        features = [
            float(request.form.get("CRIM")),
            float(request.form.get("ZN")),
            float(request.form.get("INDUS")),
            float(request.form.get("CHAS")),
            float(request.form.get("NOX")),
            float(request.form.get("RM")),
            float(request.form.get("AGE")),
            float(request.form.get("DIS")),
            float(request.form.get("RAD")),
            float(request.form.get("TAX")),
            float(request.form.get("PTRATIO")),
            float(request.form.get("B")),
            float(request.form.get("LSTAT"))
        ]

        arr = np.array([features])
        arr_scaled = scaler.transform(arr)
        arr_poly = poly.transform(arr_scaled)
        prediction = model.predict(arr_poly)[0]

        return render_template('result.html', prediction=round(prediction, 2))

    except Exception as e:
        return render_template('error.html', error=str(e), traceback=traceback.format_exc())

if __name__ == '__main__':
    app.run(debug=True)

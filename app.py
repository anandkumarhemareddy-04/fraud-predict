from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

# Load model
model = joblib.load("fraud_detection_pipeline.pkl")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        transaction_type = request.form['type']
        amount = float(request.form['amount'])
        oldbalanceOrg = float(request.form['oldbalanceOrg'])
        newbalanceOrig = float(request.form['newbalanceOrig'])
        oldbalanceDest = float(request.form['oldbalanceDest'])
        newbalanceDest = float(request.form['newbalanceDest'])

        input_data = pd.DataFrame([{
            "type": transaction_type,
            "amount": amount,
            "oldbalanceOrg": oldbalanceOrg,
            "newbalanceOrig": newbalanceOrig,
            "oldbalanceDest": oldbalanceDest,
            "newbalanceDest": newbalanceDest,
        }])

        prediction = model.predict(input_data)[0]
        prob = model.predict_proba(input_data)[0][1]

        result = "Fraud" if prediction == 1 else "Not Fraud"

        return render_template(
            'index.html',
            prediction=result,   # IMPORTANT
            prediction_text=f"Prediction: {result}",
            probability=f"Fraud Probability: {prob:.2f}"
        )

    except Exception as e:
        return render_template(
            'index.html',
            prediction_text=f"Error: {e}"
        )

if __name__ == "__main__":
    app.run(debug=True)
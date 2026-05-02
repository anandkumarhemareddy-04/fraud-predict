# 🚨 Fraud Detection System (Flask + ML)

A Machine Learning-based web application that predicts whether a financial transaction is **Fraud** or **Not Fraud** using a trained ML pipeline.

---

## 📌 Project Overview

This project uses a trained machine learning model (`fraud_detection_pipeline.pkl`) to detect fraudulent transactions based on transaction details like amount and account balances.

The application is built using Flask and provides a simple web interface for real-time predictions.

---

## 🎯 Features

* 🔍 Detects fraudulent transactions in real-time
* 📊 Displays fraud probability score
* 🧠 Uses trained ML pipeline (preprocessing + model)
* 🌐 User-friendly web interface
* ⚡ Fast predictions using `joblib`

---

## 🛠️ Tech Stack

* **Frontend:** HTML, CSS
* **Backend:** Flask (Python)
* **Machine Learning:** Scikit-learn, Pandas
* **Model File:** `.pkl` (Joblib)

---

## 📂 Project Structure

```bash
fraud-predict/
│── static/                      # CSS, JS
│── templates/                   # HTML files
│── app.py                       # Flask app
│── fraud_detection_pipeline.pkl # Trained ML model
│── AIML Dataset.csv             # Dataset :contentReference[oaicite:1]{index=1}
│── requirements.txt             # Dependencies
│── README.md                    # Documentation
```

---

## 🚀 How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/anandkumarhemareddy-04/fraud-predict.git
cd fraud-predict
```

### 2. Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python app.py
```

### 5. Open in browser

```
http://127.0.0.1:5000/
```

---

## 📊 Input Features

The model uses the following inputs:

* `type` → Transaction type
* `amount` → Transaction amount
* `oldbalanceOrg` → Sender old balance
* `newbalanceOrig` → Sender new balance
* `oldbalanceDest` → Receiver old balance
* `newbalanceDest` → Receiver new balance

---

## ⚙️ How It Works

1. User enters transaction details
2. Data is converted into a Pandas DataFrame
3. ML pipeline processes the input
4. Model predicts:

   * Fraud / Not Fraud
   * Fraud Probability

Core logic from your app: 

---

## 🧠 Model Details

* Model file: `fraud_detection_pipeline.pkl`
* Loaded using `joblib`
* Includes preprocessing + classification
* Outputs:

  * Prediction (`predict`)
  * Probability (`predict_proba`)

---

## 🔮 Future Improvements

* Improve model accuracy
* Add authentication system
* Deploy online (Render / AWS)
* Add dashboard & analytics
* Store prediction history

---

## 🤝 Contributing

Contributions are welcome! Fork the repo and submit a pull request.

---

## 📄 License

MIT License

---

## 👨‍💻 Author

**Anand Kumar Hemareddy**

---

⭐ If you like this project, give it a star on GitHub!

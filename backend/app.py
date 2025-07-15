from flask import Flask, request, render_template
import joblib
import numpy as np
import os
import pandas as pd

app = Flask(__name__, template_folder='../frontend/templates', static_folder='../frontend/static')

# Load the trained model
model_path = "../models/payment_status_model.pkl"
model = joblib.load(model_path) if os.path.exists(model_path) else None

# EDA Function
def run_eda_and_save(df):
    eda_file_path = "eda_report.txt"
    report = [
        "🟢 DATA OVERVIEW\n" + str(df.tail(10)),
        "\n\n🔢 DATA TYPES\n" + str(df.dtypes),
        "\n\n📊 NULL VALUES\n" + str(df.isnull().sum()),
        "\n\n📈 DESCRIPTIVE STATS\n" + str(df.describe())
    ]
    if 'payment_status' in df.columns:
        report.append("\n\n🔁 VALUE COUNTS\n" + str(df['payment_status'].value_counts()))
    with open(eda_file_path, "w", encoding="utf-8") as f:
        f.write("\n".join(report))
    print(f"\n✅ EDA updated and saved to {eda_file_path}")

# Home page
@app.route('/')
def home():
    return render_template('home.html')

# Prediction form page
@app.route('/predictor')
def predictor():
    df = pd.read_csv("../data/vendor_payment_data.csv")
    run_eda_and_save(df)
    return render_template('index.html')

# Prediction logic
@app.route('/predict', methods=['POST'])
def predict():
    if not model:
        return render_template('index.html', prediction="Model not found. Please train the model first.")

    invoice_amount = float(request.form['invoice_amount'])
    payment_terms = request.form['payment_terms']
    vendor_rating = float(request.form['vendor_rating'])

    payment_terms_map = {'Net 30': 0, '2/10 Net 30': 1, 'Net 45': 2, 'Net 60': 3}
    terms_encoded = payment_terms_map.get(payment_terms, 0)
    features = np.array([[invoice_amount, terms_encoded, vendor_rating]])
    prediction = model.predict(features)[0]

    status_map = {0: "Early", 1: "Late", 2: "On-time"}
    predicted_status = status_map.get(prediction, "Unknown")

    # Save prediction to dataset
    new_row = pd.DataFrame([{
        'invoice_amount': invoice_amount,
        'payment_terms': payment_terms,
        'vendor_rating': vendor_rating,
        'payment_status': predicted_status
    }])
    df = pd.read_csv("../data/vendor_payment_data.csv")
    df = pd.concat([df, new_row], ignore_index=True)
    run_eda_and_save(df)

    # Redirect to result page
    return render_template(
        'result.html',
        prediction=predicted_status,
        invoice_amount=invoice_amount,
        payment_terms=payment_terms,
        vendor_rating=vendor_rating
    )

if __name__ == '__main__':
    app.run(debug=True)

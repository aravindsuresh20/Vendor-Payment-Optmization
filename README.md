
# 🧾 Vendor Payment Status Prediction System

This project implements a web-based application using **Flask** to predict the **payment status** of vendor invoices: **Early**, **Late**, or **On-time**. It uses a **Random Forest Classifier** trained on historical vendor payment data. The system supports **Exploratory Data Analysis (EDA)** and persistent **prediction logging** to evolve with new data.

---

## 🚀 Features

- **📅 Payment Status Prediction**  
  Predicts whether a vendor payment will be:
  - **Early**
  - **Late**
  - **On-time**  
  based on:
  - Invoice Amount
  - Payment Terms
  - Vendor Rating

- **🌐 Interactive Web Interface**  
  A Flask-powered interface to input new invoice data and get instant predictions.

- **🤖 Machine Learning Model**  
  Uses a **pre-trained Random Forest Classifier** for robust classification.

- **📊 Dynamic Data Logging**  
  New inputs and predictions are appended to `vendor_payment_data.csv` for retraining.

- **🧠 Automated EDA**  
  EDA is performed on the dataset after every prediction and saved to `eda_report.txt`.

- **🛠️ Model Training Script**  
  A dedicated `train_model.py` script handles model training and persistence.

---

## 🧰 Requirements

Ensure the following Python libraries are installed:

- `Flask` – for the web framework  
- `pandas` – for data manipulation  
- `numpy` – for numerical operations  
- `scikit-learn` – for Random Forest Classifier and preprocessing  
- `joblib` – for saving and loading trained models  

Install using:

```bash
pip install -r requirements.txt
```

---

## 📁 Project Structure

```
/your-project-directory/
│── app.py                                # Main Flask application
│── train_model.py                        # Model training script
│── requirements.txt                      # Project dependencies
│── README.md                             # This documentation
│── eda_report.txt                        # EDA report (generated after predictions)
│
├── /data/
│   └── vendor_payment_data.csv           # Dataset used for training and logging
│
├── /models/
│   └── payment_status_model.pkl          # Trained Random Forest model
│
└── /frontend/
    ├── /static/                          # CSS/JS/Image assets
    └── /templates/
        ├── home.html                     # Homepage
        ├── index.html                    # Input form page
        └── result.html                   # Prediction result display
```

---

## ⚙️ Installation & Setup

1. **Clone the Repository**

```bash
git clone https://github.com/yourusername/vendor-payment-prediction.git
cd vendor-payment-prediction
```

2. **Add Your Dataset**  
Place `vendor_payment_data.csv` in the `/data/` directory. It should include:
- `invoice_amount`
- `payment_terms`
- `vendor_rating`
- `payment_status`

3. **Create `requirements.txt`**

```txt
Flask
pandas
numpy
scikit-learn
joblib
```

4. **(Optional) Create Virtual Environment**

```bash
python -m venv venv
# Activate:
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

5. **Install Dependencies**

```bash
pip install -r requirements.txt
```

6. **Train the Model**

```bash
python train_model.py
```

This saves the model as `payment_status_model.pkl` inside `/models/`.

7. **Run the Flask App**

```bash
python app.py
```

8. **Open in Browser**

Navigate to: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🧑‍💻 Usage

- **Train Model First:**  
  Run `train_model.py` to generate the `payment_status_model.pkl` file.

- **Start the App:**  
  Run `app.py` to launch the web interface.

- **Input Parameters:**  
  Enter:
  - Invoice Amount
  - Payment Terms (select)
  - Vendor Rating (numeric)

- **View Prediction:**  
  See whether the payment is likely to be **Early**, **Late**, or **On-time**.

- **Automatic Logging:**  
  Every input and prediction is saved to `vendor_payment_data.csv`.

- **EDA Report Generation:**  
  The app updates `eda_report.txt` after each prediction with:
  - Statistical summaries
  - Category distributions
  - Missing values
  - Correlations

---

## 📂 Output Files

- **`data/vendor_payment_data.csv`**  
  Updated with every new input and prediction.

- **`models/payment_status_model.pkl`**  
  Trained Random Forest Classifier used by the app.

- **`eda_report.txt`**  
  Regenerated after every prediction, providing insights on the dataset.

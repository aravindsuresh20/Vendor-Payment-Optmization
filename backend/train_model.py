import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib
import os

# Load updated dataset
df = pd.read_csv("../data/vendor_payment_data.csv")

# Encode categorical features
df['payment_terms'] = LabelEncoder().fit_transform(df['payment_terms'])
df['payment_status'] = LabelEncoder().fit_transform(df['payment_status'])

# Feature selection
X = df[['invoice_amount', 'payment_terms', 'vendor_rating']]
y = df['payment_status']

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model training
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save model
os.makedirs("../models", exist_ok=True)
joblib.dump(model, "../models/payment_status_model.pkl")
print("✅ Model trained and saved successfully.")

import streamlit as st
import pandas as pd
import numpy as np
import os
import logging
from sklearn.linear_model import LinearRegression
from sklearn.exceptions import NotFittedError

# Setup logging
os.makedirs("logs", exist_ok=True)
logging.basicConfig(
    filename="logs/app.log",
    filemode="a",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Custom title
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🏡 Real Estate Price Predictor</h1>", unsafe_allow_html=True)
st.markdown("---")

DATA_PATH = "data/final.csv"
try:
    if not os.path.exists(DATA_PATH):
        logging.error("Missing dataset file: data/final.csv")
        st.error("❌ Dataset not found. Please ensure 'data/final.csv' exists.")
        st.stop()

    df = pd.read_csv(DATA_PATH)
    logging.info("Dataset loaded successfully.")
except Exception as e:
    logging.exception("Unexpected error loading data.")
    st.error(f"Error loading dataset: {e}")
    st.stop()

drop_cols = [col for col in df.columns if 'recession' in col.lower() or 'popular' in col.lower() or 'age' in col.lower()]
df.drop(columns=drop_cols, errors='ignore', inplace=True)

try:
    X = df.drop('price', axis=1)
    y = df['price']
    model = LinearRegression()
    model.fit(X, y)
    logging.info("Model trained successfully.")
except Exception as e:
    logging.exception("Model training failed.")
    st.error(f"Error training model: {e}")
    st.stop()

feature_names = X.columns.tolist()
st.subheader("🏠 Enter Property Details")

with st.form(key='prediction_form'):
    col1, col2 = st.columns(2)
    input_data = {}

    for i, feature in enumerate(feature_names):
        col = col1 if i % 2 == 0 else col2
        try:
            if 'year' in feature.lower():
                input_data[feature] = col.number_input(f" {feature}", min_value=1800, max_value=2100, value=2020)
            elif 'bed' in feature.lower() or 'Bath' in feature.lower():
                input_data[feature] = col.slider(f" {feature}", min_value=0, max_value=10, value=2)
            elif 'lot' in feature.lower() or 'Size' in feature.lower():
                input_data[feature] = col.number_input(f" {feature}", min_value=0.0, max_value=50000.0, value=1000.0)
            elif 'basement' in feature.lower():
                choice = col.radio(f" {feature}", options=["Yes", "No"], horizontal=True)
                input_data[feature] = 1 if choice == "Yes" else 0
            elif 'property_type' in feature.lower():
                choice = col.radio(f" {feature}", options=["Bunglow", "Condo"], horizontal=True)
                input_data[feature] = 1 if choice == "Bunglow" else 0
            else:
                input_data[feature] = col.number_input(f" {feature}", value=0.0)
        except Exception as fe:
            logging.warning(f"Input field issue with '{feature}': {fe}")
            st.error(f"Issue with input field '{feature}': {fe}")

    submit = st.form_submit_button(" Predict Price")

if submit:
    try:
        input_df = pd.DataFrame([input_data])
        prediction = model.predict(input_df)[0]
        st.success(f"✅ Estimated Property Price: **${prediction:,.2f}**")
        logging.info("Prediction successful.")
    except NotFittedError:
        logging.error("Prediction failed: model not fitted.")
        st.error("Prediction failed: model not trained.")
    except Exception as pe:
        logging.exception("Prediction failed due to unexpected error.")
        st.error(f"Prediction failed: {pe}")

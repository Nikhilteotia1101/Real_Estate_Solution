# 🏡 Real Estate Price Predictor

A user-friendly Streamlit web application that predicts housing prices based on various property features using a Linear Regression model. The project demonstrates modularized machine learning development with real-time predictions, logging, and an interactive UI.

---

## 🚀 Features

✅ Interactive Streamlit UI  
✅ Custom input fields based on dataset features  
✅ Live model training on `final.csv`  
✅ Real-time price prediction  
✅ Logging for debugging and tracking  
✅ Modular code structure (`data_loader.py`, `model_trainer.py`, `app.py`)  

---

## 📁 Project Structure

Real_Estate_Solution/
│
├── app.py # Streamlit web app
├── data_loader.py # Data loading utility
├── model_trainer.py # Model training logic
├── final.csv # Dataset for training & prediction
├── requirements.txt # Python dependencies
├── app.log # Logs for model and UI activity
└── README.md # Project documentation

---

## ⚙️ Setup Instructions

### 🔁 Step 1: Clone the Repository

git clone https://github.com/Nikhilteotia1101/Real_Estate_Solution.git
cd Real_Estate_Solution
📦 Step 2: Install Dependencies

Create a virtual environment (optional but recommended), then install:
pip install -r requirements.txt

🏃 Step 3: Run the Streamlit App

streamlit run app.py

📊 Dataset
Ensure that the final.csv file is present in the root directory. This file is required to load the dataset and train the prediction model. The target variable is price, and input fields are dynamically generated from other columns.

🧠 Model Info
Algorithm: Linear Regression

Preprocessing: Drops columns with terms like recession, popular, or age

Metrics: Mean Squared Error (MSE), R² Score

Training: Done in-app using scikit-learn

📝 Logging
All events (data loading, training, prediction) are logged to logs/app.log using Python’s built-in logging module.

🎯 Future Improvements
Add advanced ML models (Random Forest, XGBoost)

Improve preprocessing (scaling, encoding, outlier removal)

Enhance UI/UX (theme, responsiveness)

Cloud deployment (Streamlit Community Cloud, AWS, Heroku)

📧 Contact
Nikhil Teotia
📍 Ottawa, Canada
🔗 LinkedIn
✉️ teot0001@algonquinlive.



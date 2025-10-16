🌾 Crop Recommendation System

A Machine Learning-based web application that predicts the best crop to grow based on soil and environmental parameters.
This project combines a Random Forest ML model with a Flask web interface for real-time crop recommendations.

🔹 Features

Predicts crop based on N, P, K, temperature, humidity, pH, and rainfall

High accuracy Random Forest model trained on historical crop data

User-friendly web interface built with Flask + Bootstrap

Real-time predictions for live sensor data

Can be extended for IoT-based precision agriculture

📁 Folder Structure
crop_recommendation/
│
├── data/
│   └── crop_data.csv              # Dataset (N, P, K, temperature, humidity, pH, rainfall, label)
│
├── model/
│   ├── crop_model.pkl             # Saved trained ML model
│   └── label_encoder.pkl          # Label encoder for crop names
│
├── train.py                       # Trains the ML model
├── predict.py                     # Predicts crop using the trained model
├── app.py                         # Flask web app for live predictions
├── requirements.txt               # Python dependencies
└── README.md                      # Project documentation

⚙️ Installation

Clone the repository:

git clone https://github.com/your-username/crop_recommendation.git
cd crop_recommendation


Install required packages:

pip install -r requirements.txt


Place your dataset in data/crop_data.csv.

🚀 Usage
1️⃣ Train the Model
python train.py


Trains the Random Forest model

Saves the model in model/crop_model.pkl and encoder in model/label_encoder.pkl

2️⃣ Predict Using Script
python predict.py


Test predictions using sample sensor data

3️⃣ Run the Web App
python app.py

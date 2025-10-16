import joblib

# Load model and encoder
model = joblib.load("model/crop_model.pkl")
encoder = joblib.load("model/label_encoder.pkl")

# Example: sensor or user data
# [N, P, K, temperature, humidity, ph, rainfall]
sensor_data = [[90, 42, 43, 21.0, 80.0, 6.5, 200.0]]

# Predict crop
prediction = model.predict(sensor_data)
crop_name = encoder.inverse_transform(prediction)

print("🌱 Recommended Crop:", crop_name[0])

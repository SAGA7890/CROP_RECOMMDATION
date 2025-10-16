from flask import Flask, request, render_template_string
import joblib
import pandas as pd

app = Flask(__name__)

# Load model and encoder
model = joblib.load("model/crop_model.pkl")
encoder = joblib.load("model/label_encoder.pkl")

# HTML template with Bootstrap
html = """
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>🌾 Crop Recommendation System</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {
            background-color: #eafaf1;
            font-family: Arial, sans-serif;
        }
        .container {
            margin-top: 50px;
            max-width: 600px;
            background: #fff;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0px 0px 15px rgba(0,0,0,0.2);
        }
        h2 {
            color: #2e7d32;
            text-align: center;
            margin-bottom: 30px;
        }
        .btn-custom {
            background-color: #2e7d32;
            color: white;
        }
        .result {
            margin-top: 20px;
            font-size: 1.3rem;
            text-align: center;
            color: #1565c0;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>🌾 Crop Recommendation System</h2>
        <form method="POST">
            <div class="mb-3">
                <label>N:</label>
                <input type="number" name="N" step="any" class="form-control" required>
            </div>
            <div class="mb-3">
                <label>P:</label>
                <input type="number" name="P" step="any" class="form-control" required>
            </div>
            <div class="mb-3">
                <label>K:</label>
                <input type="number" name="K" step="any" class="form-control" required>
            </div>
            <div class="mb-3">
                <label>Temperature (°C):</label>
                <input type="number" name="temperature" step="any" class="form-control" required>
            </div>
            <div class="mb-3">
                <label>Humidity (%):</label>
                <input type="number" name="humidity" step="any" class="form-control" required>
            </div>
            <div class="mb-3">
                <label>pH:</label>
                <input type="number" name="ph" step="any" class="form-control" required>
            </div>
            <div class="mb-3">
                <label>Rainfall (mm):</label>
                <input type="number" name="rainfall" step="any" class="form-control" required>
            </div>
            <div class="text-center">
                <button type="submit" class="btn btn-custom">Predict Crop</button>
            </div>
        </form>
        {% if crop %}
        <div class="result">
            🌱 Recommended Crop: {{ crop }}
        </div>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def home():
    crop = None
    if request.method == 'POST':
        # Read values from form
        data = {
            'N': float(request.form['N']),
            'P': float(request.form['P']),
            'K': float(request.form['K']),
            'temperature': float(request.form['temperature']),
            'humidity': float(request.form['humidity']),
            'ph': float(request.form['ph']),
            'rainfall': float(request.form['rainfall'])
        }
        # Convert to DataFrame
        columns = ['N','P','K','temperature','humidity','ph','rainfall']
        input_df = pd.DataFrame([list(data.values())], columns=columns)
        # Predict
        prediction = model.predict(input_df)
        crop = encoder.inverse_transform(prediction)[0]

    return render_template_string(html, crop=crop)

if __name__ == '__main__':
    app.run(debug=True)

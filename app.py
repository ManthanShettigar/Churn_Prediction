from flask import Flask, request, jsonify
import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from category_encoders import *
from transform import transform

app = Flask(__name__)

# Load the model and encoders
model = joblib.load('./config/best_model.pkl')


@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        print(data)
        # Create a DataFrame with the incoming data
        input_data = pd.DataFrame(data)

        # Preprocess the input data
        test_input = transform(input_data)

        # Make predictions using the model
        y_pred = model.predict(test_input)

        return jsonify({'predictions': y_pred.tolist()})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run()

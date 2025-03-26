
from flask import Flask, request, jsonify
import pandas as pd
import tensorflow as tf
from phishing_detector import dataset  # Import the dataset

# Initialize Flask app
app = Flask(__name__)

# Load the trained model
model = tf.keras.models.load_model('phishing_model.h5')  # Ensure this path is correct

# Define API route for prediction
@app.route('/predict', methods=['POST'])
def predict():
    # Get input features from the request body
    data = request.get_json()  # Data is expected to be in JSON format
    
    # Make a prediction using the model
    prediction = model.predict([data['features']])
    
    # Return the prediction result as JSON
    return jsonify({'prediction': prediction[0][0]})

# Start the Flask application
if __name__ == '__main__':
    app.run(debug=True)

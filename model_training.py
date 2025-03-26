import pandas as pd
import tensorflow as tf

# Create a dummy dataset
data = {
    'URL': ['http://example1.com', 'http://example2.com', 'http://phishingsite.com'],
    'NumDots': [2, 2, 3],
    'SubdomainLevel': [1, 1, 2],
    'PathLevel': [2, 3, 1],
    'Label': ['legitimate', 'legitimate', 'phishing']
}

# Convert to pandas DataFrame
dataset = pd.DataFrame(data)

# Define features and labels
features = dataset[['NumDots', 'SubdomainLevel', 'PathLevel']]  # Input features
labels = dataset['Label'].map({'legitimate': 0, 'phishing': 1})  # Labels (0 for legitimate, 1 for phishing)

# Build and compile the model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(features.shape[1],)),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')  # Binary classification
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(features, labels, epochs=10, batch_size=1)

# Save the trained model
model.save('phishing_model.h5')  # This will save the model as phishing_model.h5

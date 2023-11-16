from tensorflow import keras
from sklearn.preprocessing import StandardScaler

from dataset import rows, columns, test
import pandas as pd
import numpy as np

df = pd.DataFrame(rows, columns=columns)

# Extracting features and label
features = df[["f_1", "f_2", "f_3", "f_4"]]
label = df["l_1"]


# Convert the test set to a DataFrame
test_df = pd.DataFrame(test, columns=columns[:-1])

# Building a simple neural network model
model = keras.Sequential([
    keras.layers.Dense(64, activation='relu', input_shape=(4,)),
    keras.layers.Dense(1)
])

# Compiling the model
model.compile(optimizer='adam', loss='mean_squared_error')
# Generate additional training features by averaging existing data
num_additional_samples = 10

for _ in range(num_additional_samples):
    # Average the existing features
    new_features = np.mean(features.values, axis=0)

    # Add some noise to simulate variation
    new_features += np.random.normal(0, 0.001, new_features.shape)

    # Predict the corresponding label using the trained model
    new_label = model.predict(new_features.reshape(1, -1))

    # Append the new features and label to the DataFrame
    df = df._append({"f_1": new_features[0], "f_2": new_features[1], "f_3": new_features[2], "f_4": new_features[3], "l_1": new_label[0, 0]}, ignore_index=True)

# Extract the updated features and label
features_updated = df[["f_1", "f_2", "f_3", "f_4"]]
label_updated = df["l_1"]


# Train the model with the updated data
model.fit(features_updated, label_updated, epochs=100, batch_size=2)
# Make predictions on the test set
predictions = model.predict(test)

# Print the predictions
print("Predictions on the test set:")
predictions_list = predictions.tolist()

for i in range(len(test)):
    print(f"Input Feature: {test[i]} \n Output Label: {predictions_list[i][0]}")


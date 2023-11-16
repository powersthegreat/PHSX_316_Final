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

# Training the model using all data
model.fit(features, label, epochs=100, batch_size=2)

# Make predictions on the test set
predictions = model.predict(test)

# Print the predictions
print("Predictions on the test set:")
predictions_list = predictions.tolist()

for i in range(len(test)):
    print(f"Input Feature: {test[i]} \n Output Label: {predictions_list[i][0]}")


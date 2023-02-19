# Import necessary libraries
import pandas as pd
from sklearn.linear_model import LinearRegression

# Load the data
data = pd.read_csv("data.csv")

# Split the data into input and output variables
X = data.iloc[:, :-1].values
y = data.iloc[:, -1].values

# Train the model
model = LinearRegression()
model.fit(X, y)

# Make predictions on new data
new_data = [[5.1, 3.5, 1.4, 0.2]]
prediction = model.predict(new_data)

# Print the prediction
print(prediction)

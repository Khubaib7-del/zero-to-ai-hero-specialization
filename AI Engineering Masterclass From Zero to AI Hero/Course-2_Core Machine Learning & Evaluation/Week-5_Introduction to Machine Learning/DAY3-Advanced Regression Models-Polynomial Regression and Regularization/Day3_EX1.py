#implement Polynomial Regression and Visualize the fit

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

#Load the California housing dataset
data = fetch_california_housing(as_frame=True)
df=data.frame

# Select features (Median Income) and target (Median House Value)
X = df[['MedInc']]
y = df['MedHouseVal']

# Transform feature to polynomial features
poly = PolynomialFeatures(degree=2)  # You can change the degree to see different fits
X_poly = poly.fit_transform(X)

#Fit Polynomial Regression model
model = LinearRegression()
model.fit(X_poly, y)

#Make Predictions using Linear Regression
y_pred = model.predict(X_poly)


#Plot the actual VS predicted values
plt.figure(figsize=(10, 6))
plt.scatter(X, y, color='blue', label='Actual values')
plt.scatter(X, y_pred, color='red', label='Predicted values')
plt.title('Polynomial Regression Fit')
plt.xlabel('Median Income')
plt.ylabel('Median House Value')
plt.legend()
plt.show()

# Evalute the model using Mean Squared Error
mse = mean_squared_error(y, y_pred)
print(f'Mean Squared Error: {mse}')

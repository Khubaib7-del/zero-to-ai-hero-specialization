#implement Polynomial Regression and Visualize the fit

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import Lasso, LinearRegression,Ridge
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

#Load the California housing dataset
data = fetch_california_housing(as_frame=True)
df=data.frame

# Select features (Median Income) and target (Median House Value)
X = df[['MedInc']]
y = df['MedHouseVal']

# Transform feature to polynomial features
poly = PolynomialFeatures(degree=2)  # You can change the degree to see different fits
X_poly = poly.fit_transform(X)


# split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_poly, y, test_size=0.2, random_state=42)


# Ridge Regression
ridge = Ridge(alpha=1.0)
ridge.fit(X_train, y_train)
y_pred_ridge = ridge.predict(X_test)

# Lasso Regression
lasso = Lasso(alpha=0.1)
lasso.fit(X_train, y_train)
y_pred_lasso = lasso.predict(X_test)

# Evaluate Ridge Regression
mse_ridge = mean_squared_error(y_test, y_pred_ridge)
print(f"Ridge Regression Mean Squared Error: {mse_ridge}")

# Evaluate Lasso Regression
mse_lasso = mean_squared_error(y_test, y_pred_lasso)
print(f"Lasso Regression Mean Squared Error: {mse_lasso}")

# Visualize Ridge VS Lasso Predictions
plt.figure(figsize=(12, 6))
plt.scatter(X_test[:, 1], y_test, color='blue', label='Actual Data', alpha=0.5)
# Sort the test data for a better visualization of the fit                  
plt.scatter(X_test[:, 1], y_pred_ridge, color='red', label='Ridge Predictions', alpha=0.5)
plt.scatter(X_test[:, 1], y_pred_lasso, color='green', label='Lasso Predictions', alpha=0.5)
plt.title('Ridge vs Lasso Regression Predictions')
plt.xlabel('Median Income')
plt.ylabel('Median House Value')
plt.legend()
plt.show()

#implement a simple Linear Regtression Model Using Scikit-Learn

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression   
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Generate Synthetic Data

np.random.seed(42)
X=np.random.rand(100,1)*100
y=2*X+np.random.randn(100,1)*2

# Split Data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)   

# fit Linear Regression Model
model=LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred=model.predict(X_test)

#print coeffircients
print("Slope", model.coef_[0][0])
print("Intercept", model.intercept_[0])

# Visualize the regression line
plt.scatter(X_test, y_test, color='blue', label='Actual Data')
plt.plot(X_test, y_pred, color='red', label='Regression Line')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Simple Linear Regression')
plt.legend()
plt.show()


# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)   
print("Mean Squared Error:", mse)
print("R-squared:", r2)
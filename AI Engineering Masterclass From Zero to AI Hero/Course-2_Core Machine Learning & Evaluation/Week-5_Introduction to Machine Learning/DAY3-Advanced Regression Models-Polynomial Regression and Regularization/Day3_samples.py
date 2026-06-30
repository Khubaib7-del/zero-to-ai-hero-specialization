import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


# Generate synthetic data
np.random.seed(42)

X=np.random.rand(100,1)*10
y=3*X**2 + 2*X + 1 + np.random.randn(100,1)*5

# Transform features to polynomial features
poly_features=PolynomialFeatures(degree=2, include_bias=False)
X_poly=poly_features.fit_transform(X)


# Fit linear regression model
model=LinearRegression()
model.fit(X_poly, y)
y_pred=model.predict(X_poly)

#Plotting the results
plt.scatter(X, y, color='blue', label='Data points')
plt.plot(X, y_pred, color='red', label='Polynomial regression')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.show()

# Calculate and print the mean squared error
mse=mean_squared_error(y, y_pred)   
print(f'Mean Squared Error: {mse:.2f}')

import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# load Bike sharing Dataset
url="https://raw.githubusercontent.com/PacktPublishing/AI-Engineering-Masterclass-From-Zero-to-AI-Hero/main/Week6/Day5/bike_sharing_daily.csv"
df=pd.read_csv(url)

# display the information of the dataset
# print("Information of the dataset:")
# print(df.info())

# display first 5 rows of the dataset
# print("First 5 rows of the dataset:")
# print(df.head())

# Convert the 'datetime' column to datetime type
df['dteday'] = pd.to_datetime(df['dteday'])

# create a new column 'day_of_week' that contains the day of the week for each date
df['day_of_week'] = df['dteday'].dt.day_name()
df['month'] = df['dteday'].dt.month
df['year'] = df['dteday'].dt.year

# Dissplay the new features created
# print("New features created:")
# print(df[['dteday', 'day_of_week', 'month', 'year']].head())

# Select feature and target variable
X = df[['temp']]
y = df['cnt']

# Apply Polynomial Transformation
poly = PolynomialFeatures(degree=2, include_bias=False)
X_poly = poly.fit_transform(X)

# Display the transformed features
# print("Original and Transformed features:")
# print("Original features:")
# print(X.head())
# print("Transformed features:")
# print(X_poly[:5])  # Display first 5 rows of transformed features

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
X_poly_train,X_poly_test=train_test_split(X_poly, test_size=0.2, random_state=42)
# Create a Linear Regression model
model_original = LinearRegression()
# Train the model with original features
model_original.fit(X_train, y_train)
# Predict on the test set with original features
y_pred_original = model_original.predict(X_test)
# Calculate Mean Squared Error for original features
mse_original = mean_squared_error(y_test, y_pred_original)

# Create a Linear Regression model for polynomial features
model_poly = LinearRegression()
# Train the model with polynomial features
model_poly.fit(X_poly_train, y_train)
# Predict on the test set with polynomial features
y_pred_poly = model_poly.predict(X_poly_test)
# Calculate Mean Squared Error for polynomial features
mse_poly = mean_squared_error(y_test, y_pred_poly)

# Compare the Mean Squared Errors
print(f"Mean Squared Error with original features: {mse_original}")
print(f"Mean Squared Error with polynomial features: {mse_poly}")
from sklearn.datasets import load_iris
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import MinMaxScaler, StandardScaler


# Load Iris dataset
iris = load_iris()
X=pd.DataFrame(data=iris.data, columns=iris.feature_names)

# Display dataset information
print("Dataset Information:")
print(X.describe())
print("Target Classes:")
print(iris.target_names)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, iris.target, test_size=0.2, random_state=42)

# Train the K-Nearest Neighbors classifier
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

# Make predictions on the test set
y_pred = knn.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")

# Appply Min-Max Scaling to the features
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

# Split the scaled dataset into training and testing sets
X_train_scaled, X_test_scaled, y_train_scaled, y_test_scaled = train_test_split(X_scaled, iris.target, test_size=0.2, random_state=42)

# Train the K-Nearest Neighbors classifier on scaled data
knn_scaled = KNeighborsClassifier(n_neighbors=3)
knn_scaled.fit(X_train_scaled, y_train_scaled)

# Make predictions on the scaled test set
y_pred_scaled = knn_scaled.predict(X_test_scaled)

# Calculate accuracy for scaled data
accuracy_scaled = accuracy_score(y_test_scaled, y_pred_scaled)
print(f"Accuracy after Min-Max Scaling: {accuracy_scaled}")

# Apply Standard Scaling to the features
scaler_standard = StandardScaler()
X_standard_scaled = scaler_standard.fit_transform(X)

# Split the standard scaled dataset into training and testing sets
X_train_standard, X_test_standard, y_train_standard, y_test_standard = train_test_split(X_standard_scaled, iris.target, test_size=0.2, random_state=42)

# Train the K-Nearest Neighbors classifier on standard scaled data
knn_standard = KNeighborsClassifier(n_neighbors=3)
knn_standard.fit(X_train_standard, y_train_standard)

# Make predictions on the standard scaled test set
y_pred_standard = knn_standard.predict(X_test_standard)

# Calculate accuracy for standard scaled data
accuracy_standard = accuracy_score(y_test_standard, y_pred_standard)
print(f"Accuracy after Standard Scaling: {accuracy_standard}")
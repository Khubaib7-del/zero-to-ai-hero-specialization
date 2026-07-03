from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,classification_report
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression


# Load the iris dataset
data = load_iris()
X,y=data.data,data.target

# Split the Dataset into training and testing sets
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

# Scale the features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


# Train a Logistic Regression model
logistic_model = LogisticRegression(max_iter=200)
logistic_model.fit(X_train, y_train)


# Make predictions using the Logistic Regression model
y_pred_logistic = logistic_model.predict(X_test)

# Evaluate the Logistic Regression model
accuracy_logistic = accuracy_score(y_test, y_pred_logistic)
print(f"Accuracy of Logistic Regression: {accuracy_logistic}")

# Evaluate k-NN
best_k=5
knn=KNeighborsClassifier(n_neighbors=best_k)
knn.fit(X_train,y_train)
y_pred_knn=knn.predict(X_test)
accuracy_knn=accuracy_score(y_test,y_pred_knn)
print(f"Accuracy of k-NN (k={best_k}): {accuracy_knn}")

# Dtailed comparison of the two models
print("\nDetailed Comparison:")

print("Logistic Regression Classification Report:")
print(classification_report(y_test, y_pred_logistic))

print("k-NN Classification Report:")
print(classification_report(y_test, y_pred_knn))


# # Create and train the k-NN classifier
# for k in range(1, 11):
#     knn = KNeighborsClassifier(n_neighbors=k)
#     knn.fit(X_train, y_train)
    
#     # Make predictions
#     y_pred = knn.predict(X_test)
    
#     # Evaluate the model
#     accuracy = accuracy_score(y_test, y_pred)
#     print(f"Accuracy for k={k}: {accuracy}")
    
#     # Print classification report
#     print(f"Classification Report for k={k}:")
#     print(classification_report(y_test, y_pred))

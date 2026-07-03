import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix


# Load Telco Customer Churn Dataset
telco_url = 'https://raw.githubusercontent.com/IBM/telco-customer-churn-on-icp4d/master/data/Telco-Customer-Churn.csv'
telco_data = pd.read_csv(telco_url)

# Clean and encode the target
telco_data['TotalCharges'] = pd.to_numeric(telco_data['TotalCharges'], errors='coerce')
telco_data['TotalCharges'] = telco_data['TotalCharges'].fillna(telco_data['TotalCharges'].median())

# Encode categorical variables
le = LabelEncoder()
telco_data['churn'] = le.fit_transform(telco_data['Churn'])

# Define features and target variable
X = telco_data.drop(columns=['Churn', 'churn', 'customerID'])
X = pd.get_dummies(X, drop_first=True)
y = telco_data['churn']

#Scale the features
scaler = StandardScaler()
X_s = scaler.fit_transform(X)

# Split  dataset
X_train, X_test, y_train, y_test = train_test_split(X_s, y, test_size=0.2, random_state=42)

# Train a logistic regression model
lr_model = LogisticRegression(max_iter=1000)
lr_model.fit(X_train, y_train)

# Train a KNN model
knn_model = KNeighborsClassifier(n_neighbors=5)
knn_model.fit(X_train, y_train)

# Make predictions on the test set
lr_predictions = lr_model.predict(X_test)
knn_predictions = knn_model.predict(X_test)

# Evaluate the models
print("Logistic Regression Results:")
print(classification_report(y_test, lr_predictions))
print("Confusion Matrix:")
print(confusion_matrix(y_test, lr_predictions))

print("\nKNN Results:")
print(classification_report(y_test, knn_predictions))
print("Confusion Matrix:")
print(confusion_matrix(y_test, knn_predictions))

# # Inspect Telco data
# print(telco_data.info())
# print(telco_data.describe())

# # Visualize relationships in Telco data
# sns.countplot(x='Churn', data=telco_data)
# plt.title('Churn Count')
# plt.show()

# # Missing values in Telco data
# print("missing values in Telco data:\n", telco_data.isnull().sum()) 
# telco_data.fillna(telco_data.mean(), inplace=True)  # Fill missing values with mean for numerical columns
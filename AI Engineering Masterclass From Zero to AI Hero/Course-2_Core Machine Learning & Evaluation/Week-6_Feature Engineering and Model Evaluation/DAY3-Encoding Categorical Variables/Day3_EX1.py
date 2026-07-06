import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression

# Load the dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

# Display dataset information
print("Dataset Information:")
print(df.info())

# Preview the first few rows of the dataset
print("\nFirst 5 rows of the dataset:")
print(df.head())


# Apply one-hot encoding 
df_one_hot=pd.get_dummies(df, columns=['Sex', 'Embarked'], drop_first=True)

# Display the first few rows of the one-hot encoded dataset
print("\nFirst 5 rows of the one-hot encoded dataset:")
print(df_one_hot.head())

# Apply Label Encoding
label_encoder = LabelEncoder()
df['pclass_encoded'] = label_encoder.fit_transform(df['Pclass'])

# Display the first few rows of the dataset with label encoding
print("\nFirst 5 rows of the dataset with label encoding:")
print(df[['Pclass', 'pclass_encoded']].head())

# Apply Frequency Encoding
df['Ticket_freq_encoded'] = df['Ticket'].map(df['Ticket'].value_counts())
# Display the first few rows of the dataset with frequency encoding
print("\nFirst 5 rows of the dataset with frequency encoding:")
print(df[['Ticket', 'Ticket_freq_encoded']].head())


X=df_one_hot.drop(['Survived', 'Name', 'Ticket', 'Cabin'])
y=df['Survived']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y,train_size=0.8, random_state=42)

# Train a Logistic Regression model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Calculate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
print(f"\nModel Accuracy: {accuracy:.2f}")


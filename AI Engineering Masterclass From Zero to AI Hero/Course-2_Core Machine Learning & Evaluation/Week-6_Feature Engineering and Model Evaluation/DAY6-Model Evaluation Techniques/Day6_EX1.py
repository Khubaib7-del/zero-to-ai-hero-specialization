from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report,ConfusionMatrixDisplay
import matplotlib.pyplot as plt

# Load the iris dataset
iris = load_iris()
X=iris.data
y=(iris.target==0).astype(int)  # Convert to binary classification problem (class 2 vs others)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Calculate the confusion matrix
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(cm)
disp= ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=['Not Class 0', 'Class 0'])
disp.plot(cmap='Blues')
plt.title("Confusion Matrix")
plt.show()

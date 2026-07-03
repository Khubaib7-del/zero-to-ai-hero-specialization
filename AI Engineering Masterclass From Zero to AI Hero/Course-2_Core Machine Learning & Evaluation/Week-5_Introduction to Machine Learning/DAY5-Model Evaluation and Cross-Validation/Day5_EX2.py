from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris
from sklearn.metrics import confusion_matrix, classification_report,ConfusionMatrixDisplay
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Load Dataset
data=load_iris()
X, y=data.data, data.target

# Split Dataset
X_train, X_test, y_train, y_test=train_test_split(X,y,test_size=0.2,random_state=42)

# Train Logistic Regression Model
model=LogisticRegression(max_iter=200)
model.fit(X_train,y_train)

# Predict on Test Set
y_pred=model.predict(X_test)

# Generate the confusion matrix
cm=confusion_matrix(y_test,y_pred)

# Display confuaion matrix
disp=ConfusionMatrixDisplay(confusion_matrix=cm,display_labels=data.target_names)
disp.plot(cmap='Blues')
plt.show()

# Print classification report
print("Classification Report:")
print(classification_report(y_test,y_pred,target_names=data.target_names))


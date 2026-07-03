from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score,KFold
from sklearn.ensemble import  RandomForestClassifier

# Load datasets
data = load_iris()
X, y= data.data, data.target

# Initialize the classifier
model = RandomForestClassifier(random_state=42)

# perform k-fold cross-validation
kfold = KFold(n_splits=5, shuffle=True, random_state=42)
cv_scores=cross_val_score(model, X, y, cv=kfold)

# Print the cross-validation scores
print("Cross-validation scores:", cv_scores)
print("Mean cross-validation score:", cv_scores.mean())
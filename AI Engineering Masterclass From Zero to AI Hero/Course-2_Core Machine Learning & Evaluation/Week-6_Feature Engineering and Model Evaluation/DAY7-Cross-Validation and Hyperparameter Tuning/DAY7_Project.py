import pandas as pd
from sklearn.preprocessing import StandardScaler,OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import GridSearchCV, cross_val_predict
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

# Load the dataset
url="https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

# Display Slected features
df=df[[ 'Pclass', 'Sex', 'Age',  'Fare','Embarked','Survived']]

    
# Handle missing values
df['Age'].fillna(df['Age'].median(), inplace=True)
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

# Define the features and target variable
X = df.drop('Survived', axis=1)
y = df['Survived']

# Define the column transformer for preprocessing
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), ['Age', 'Fare']),
        ('cat', OneHotEncoder(), ['Pclass', 'Sex', 'Embarked'])
    ])

X_preprocessed = preprocessor.fit_transform(X)

# Define the models
log_model = LogisticRegression()
log_scores = cross_val_predict(log_model, X_preprocessed, y, cv=5, scoring='accuracy')
print("Logistic Regression Cross-Validation Scores:", f"{log_scores.mean():.2f}")

# Train and evaluate the Random Forest model
rf_model = RandomForestClassifier()
rf_scores = cross_val_predict(rf_model, X_preprocessed, y, cv=5, scoring='accuracy')
print("Random Forest Cross-Validation Scores:", f"{rf_scores.mean():.2f}")

#Define the hyperparameter grid 
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [None, 10, 20, 30],
    'min_samples_split': [2, 5, 10],
}

# perform hyperparameter tuning using GridSearchCV
grid_search=GridSearchCV(estimator=rf_model, param_grid=param_grid, cv=5, scoring='accuracy', n_jobs=-1)
grid_search.fit(X_preprocessed, y)

# Print the best hyperparameters and the corresponding score
print("Best Hyperparameters:", grid_search.best_params_)
print("Best Cross-Validation Score:", f"{grid_search.best_score_:.2f}")

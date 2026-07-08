from sklearn.datasets import load_diabetes
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.feature_selection import mutual_info_regression

# Load the diabetes dataset
diabetes = load_diabetes()
df=pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
df['target'] = diabetes.target

# Display  Dataset Information
# print("Dataset Information:")
# print(df.info())

# print("\nFirst 5 rows of the dataset:")
# print(df.head())


# Calculate the correlation matrix
corr_matrix = df.corr()

# Set up the matplotlib figure
# plt.figure(figsize=(12, 8))
# sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0)     
# plt.title("Correlation Matrix")
# plt.show()

#Selecting features with high correlation with the target variable
# print("Features with high correlation with the target variable:")
# target_corr = corr_matrix['target'].abs().sort_values(ascending=False)
# high_corr_features = target_corr[target_corr > 0.3].index.tolist()
# print(high_corr_features)

# seaparate the features and target variable
X = df.drop('target', axis=1)
y = df['target']

# Calculate mutual information between each feature and the target variable

mutual_info = mutual_info_regression(X, y)

# Create a DataFrame to display the mutual information scores
mi_df = pd.DataFrame({'Feature': X.columns, 'Mutual_Info': mutual_info})
mi_df=mi_df.sort_values(by='Mutual_Info', ascending=False)

# print ("\nMutual Information Scores:")
# print(mi_df)

from sklearn.ensemble import RandomForestRegressor
import numpy as np

# Train a Random Forest model to get feature importances
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

# Get feature importances
importances = model.feature_importances_
importance_df=pd.DataFrame({'Feature': X.columns, 'Importance': importances})
importance_df=importance_df.sort_values(by='Importance', ascending=False)

print("\nFeature Importances from Random Forest:")
print(importance_df)

# Plot feature importances
plt.figure(figsize=(10, 6))
plt.barh(importance_df['Feature'], importance_df['Importance'], color='skyblue')
plt.gca().invert_yaxis()  # Invert y-axis to have the most important feature on top 
plt.title('Feature Importances from Random Forest')
plt.xlabel('Importance')
plt.ylabel('Feature')
plt.show()
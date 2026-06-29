#url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"

import pandas as pd
from sklearn.model_selection import train_test_split
import seaborn as sns
import matplotlib.pyplot as plt
# Load Dataset

url="https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
df=pd.read_csv(url)

#Define Features and target
features=df[['total_bill', 'size']]
target=df['tip']

print("Features:",features.head())
print("Target:",target.head())

X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

print("Training Features Shape:", X_train.shape)
print("Testing Features Shape:", X_test.shape)
print("Training Target Shape:", y_train.shape)
print("Testing Target Shape:", y_test.shape)


# Visualize the relationship
sns.pairplot(df,x_vars=['total_bill', 'size'], y_vars='tip', height=5, aspect=0.8, kind='scatter')
plt.title("Scatter Plot of Features vs Target")
plt.show()
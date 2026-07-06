import pandas as pd

# Load Titanic dataset
url="https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df=pd.read_csv(url)

# Display dataset information
print("Dataset Information:")
print(df.info())

# Preview the first 5 rows of the dataset
print("First 5 rows of the dataset:")
print(df.head())

# Seperate features 
categorical_features = df.select_dtypes(include=['object']).columns
numerical_features = df.select_dtypes(include=['int64', 'float64']).columns


print("Categorical Features:")
print(categorical_features)
print("Numerical Features:")
print(numerical_features)

# Display Summary of Categorical Features
print("Summary of Categorical Features:")
for col in categorical_features:
    print(f"\nColumn: {col}")
    print(df[col].value_counts())
    print(df[col].value_counts(normalize=True))

# Display Summary of Numerical Features
print("Summary of Numerical Features:")
for col in numerical_features:
    print(f"\nColumn: {col}")
    print(df[col].describe())
    

    
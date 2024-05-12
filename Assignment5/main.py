import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, roc_auc_score, classification_report


# Load data from Excel file
data = pd.read_excel("data.xlsx", sheet_name="Insurance Quotes", parse_dates=['car_immatriculation_date', 'birth_date'])

# Convert 'birth_date' to datetime
data['birth_date'] = pd.to_datetime(data['birth_date'], errors='coerce')

# Calculate client_age
current_date = pd.Timestamp('now')
data['client_age'] = (current_date - data['birth_date']).dt.days / 365.25

# Handle missing values for 'client_age' and other numerical columns
data['client_age'].fillna(data['client_age'].median(), inplace=True)
numerical_columns = ['driver_injury', 'legal_protection', 'collision', 'theft_fire', 'kasko', 'license_revoked']
for column in numerical_columns:
    data[column].fillna(data[column].median(), inplace=True)

# Convert categorical variables to dummy variables
categorical_columns = ['driving_type', 'car_brand', 'car_model', 'gender', 'county', 'base_type', 'operating_system']
data = pd.get_dummies(data, columns=categorical_columns, drop_first=True)

# Identify columns with low variance
low_variance_cols = [col for col in data.columns if data[col].nunique() == 1]

# Drop these columns
data.drop(columns=low_variance_cols, inplace=True)


threshold = 10  

frequent_columns = [col for col in data.columns if 'county_' in col and data[col].sum() > threshold]
data = data[frequent_columns + [col for col in data.columns if 'county_' not in col]]  # Keep non-county columns

# Use the data DataFrame for splitting
X = data.drop('issued', axis=1)
y = data['issued']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the RandomForest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predict on the testing set
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
roc_auc = roc_auc_score(y_test, model.predict_proba(X_test)[:, 1])
report = classification_report(y_test, y_pred)

# Output the evaluation results
print("Accuracy:", accuracy)
print("ROC-AUC:", roc_auc)
print("Classification Report:\n", report)



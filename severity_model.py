import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.impute import SimpleImputer
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score, recall_score, f1_score, confusion_matrix

# Load the dataset
df = pd.read_csv('tx_accidents.csv')

# Display the first few rows of the dataset
df_head = df.head()

# Summary statistics
summary_stats = df.describe()

# Information about the dataset, including the datatype of each column
df_info = df.info()

print(df_head, summary_stats, df_info)

# Dropping columns with excessive missing values or those not relevant for our initial models
columns_to_drop = ['End_Lat', 'End_Lng', 'Wind_Chill(F)', 'Precipitation(in)', 'Unnamed: 0', 'ID', 'Source', 'Description', 'Street', 'Zipcode', 'Country', 'Weather_Timestamp', 'Airport_Code']
df_cleaned = df.drop(columns=columns_to_drop)

# Imputing missing values for numerical columns with their median
num_cols = df_cleaned.select_dtypes(include=['float64', 'int64']).columns
for col in num_cols:
    df_cleaned[col].fillna(df_cleaned[col].median(), inplace=True)

# Encoding categorical variables that are relevant
cat_cols = df_cleaned.select_dtypes(include=['object', 'bool']).columns
label_encoders = {}
for col in cat_cols:
    le = LabelEncoder()
    df_cleaned[col] = le.fit_transform(df_cleaned[col].astype(str))
    label_encoders[col] = le

# Checking the cleanup results
df_cleaned_info = df_cleaned.info()
df_cleaned_head = df_cleaned.head()

print(df_cleaned_info, df_cleaned_head)

X = df_cleaned.drop('Severity', axis=1)
y = df_cleaned['Severity']

# Splitting into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Checking the shape of the splits to confirm successful splitting
(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

rf_clf = RandomForestClassifier(n_estimators=100, random_state=42)

# Training the model
rf_clf.fit(X_train, y_train)

# Predicting on the test set
y_pred = rf_clf.predict(X_test)

# Evaluating the model
accuracy = accuracy_score(y_test, y_pred)
print(accuracy)

# Calculating precision, recall, and F1-score
precision = precision_score(y_test, y_pred, average='macro')
recall = recall_score(y_test, y_pred, average='macro')
f1 = f1_score(y_test, y_pred, average='macro')

# Generating the confusion matrix
conf_matrix = confusion_matrix(y_test, y_pred)

print(precision, recall, f1, conf_matrix)
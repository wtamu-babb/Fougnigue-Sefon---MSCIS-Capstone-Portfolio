import numpy as np
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from lightgbm import LGBMClassifier

# Path for saving models and preprocessor
save_path = "C:/Users/sefon/OneDrive/Documents/WTAMU/Spring24/Capstone/Project/"

# Load the dataset
file_path = 'C:/Users/sefon/Downloads/online_shoppers_intention.csv'
df = pd.read_csv(file_path)

# Define numerical and categorical columns
numeric_features = ['Administrative', 'Administrative_Duration', 'Informational', 'Informational_Duration',
                    'ProductRelated', 'ProductRelated_Duration', 'BounceRates', 'ExitRates', 'PageValues']
categorical_features = ['Month', 'OperatingSystems', 'Browser', 'Region', 'TrafficType', 'VisitorType', 'Weekend']

# Data preprocessing with ColumnTransformer
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numeric_features),
        ('cat', OneHotEncoder(), categorical_features)
    ])

# Fit the preprocessor and transform the features
X = preprocessor.fit_transform(df.drop('Revenue', axis=1))
y = df['Revenue']

# Save the fitted preprocessor
joblib.dump(preprocessor, save_path + 'preprocessor.pkl')

# Splitting data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42, stratify=y)

# Logistic Regression Model
lr_model = LogisticRegression(max_iter=1000)
lr_model.fit(X_train, y_train)
joblib.dump(lr_model, save_path + 'logistic_regression_model.pkl')

# Naive Bayes Classifier (requires dense matrix)
X_train_dense = X_train.toarray()  # Convert sparse matrix to dense
nb_model = GaussianNB()
nb_model.fit(X_train_dense, y_train)
joblib.dump(nb_model, save_path + 'naive_bayes_model.pkl')

# LightGBM Classifier
lgbm_model = LGBMClassifier()
lgbm_model.fit(X_train, y_train)
joblib.dump(lgbm_model, save_path + 'lightgbm_model.pkl')
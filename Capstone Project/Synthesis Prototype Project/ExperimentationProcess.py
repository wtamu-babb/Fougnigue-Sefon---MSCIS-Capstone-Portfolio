import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier, VotingClassifier
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neural_network import MLPClassifier
from sklearn.tree import DecisionTreeClassifier
from xgboost import XGBClassifier
from lightgbm import LGBMClassifier
from catboost import CatBoostClassifier


# Load the dataset
file_path = 'C:/Users/sefon/Downloads/online_shoppers_intention.csv'
df = pd.read_csv(file_path)

# Display initial data and basic statistics
print("Initial data preview:")
print(df.head())
print("\nDataset information:")
print(df.info())
print("\nDataset statistics:")
print(df.describe())
print("\nBalance of target variable 'Revenue':")
print(df['Revenue'].value_counts())

# Define numerical and categorical columns
numeric_features = ['Administrative', 'Informational', 'ProductRelated',
                    'Administrative_Duration', 'Informational_Duration', 
                    'ProductRelated_Duration', 'BounceRates', 'ExitRates', 'PageValues']
categorical_features = ['Month', 'OperatingSystems', 'Browser', 'Region', 'TrafficType', 
                        'VisitorType', 'Weekend']

# Display correlation matrix
numeric_df = df[numeric_features]
print("\nCorrelation matrix of numeric features:")
print(numeric_df.corr())

# Data preprocessing with ColumnTransformer
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numeric_features),
        ('cat', OneHotEncoder(), categorical_features)
    ])

# Prepare feature matrix X and target vector y
X = preprocessor.fit_transform(df.drop('Revenue', axis=1))
y = df['Revenue']

# Splitting data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42, stratify=y)

# Logistic Regression Model
lr_model = LogisticRegression(max_iter=1000)
lr_model.fit(X_train, y_train)
print("\nLogistic Regression Confusion Matrix:")
print(confusion_matrix(y_test, lr_model.predict(X_test)))
print("\nLogistic Regression Evaluation:")
print(classification_report(y_test, lr_model.predict(X_test)))


# Gradient Boosting Classifier
gbm_model = GradientBoostingClassifier(n_estimators=100, learning_rate=0.1, random_state=42)
gbm_model.fit(X_train, y_train)
print("\nGradient Boosting Confusion Matrix:")
print(confusion_matrix(y_test, gbm_model.predict(X_test)))
print("\nGradient Boosting Machine Evaluation:")
print(classification_report(y_test, gbm_model.predict(X_test)))

# Random Forest Classifier
rf_model = RandomForestClassifier(n_estimators=100, class_weight='balanced', random_state=42)
rf_model.fit(X_train, y_train)
print("\nRandom Forest Confusion Matrix:")
print(confusion_matrix(y_test, rf_model.predict(X_test)))
print("\nRandom Forest Evaluation:")
print(classification_report(y_test, rf_model.predict(X_test)))

# Support Vector Machine Classifier
svm_model = SVC(class_weight={False: 1, True: 5}, kernel='linear', random_state=42)
svm_model.fit(X_train, y_train)
print("\nSupport Vector Machine Confusion Matrix:")
print(confusion_matrix(y_test, svm_model.predict(X_test)))
print("\nSupport Vector Machine Evaluation:")
print(classification_report(y_test, svm_model.predict(X_test)))

# K-Nearest Neighbors Classifier
knn_model = KNeighborsClassifier(n_neighbors=5)
knn_model.fit(X_train, y_train)
print("\nK-Nearest Neighbors Confusion Matrix:")
print(confusion_matrix(y_test, knn_model.predict(X_test)))
print("\nK-Nearest Neighbors Evaluation:")
print(classification_report(y_test, knn_model.predict(X_test)))

# Gaussian Naive Bayes Classifier
X_train_dense = X_train.toarray()  # Converting sparse to dense for NB compatibility
X_test_dense = X_test.toarray()
nb_model = GaussianNB()
nb_model.fit(X_train_dense, y_train)
print("\nNaive Bayes Confusion Matrix:")
print(confusion_matrix(y_test, nb_model.predict(X_test_dense)))
print("\nNaive Bayes Evaluation:")
print(classification_report(y_test, nb_model.predict(X_test_dense)))

# Multi-layer Perceptron Classifier
mlp_model = MLPClassifier(hidden_layer_sizes=(100,), max_iter=300, activation='relu', solver='adam', random_state=42)
mlp_model.fit(X_train, y_train)
print("\nMulti-layer Perceptron Confusion Matrix:")
print(confusion_matrix(y_test, mlp_model.predict(X_test)))
print("\nMulti-layer Perceptron Evaluation:")
print(classification_report(y_test, mlp_model.predict(X_test)))

# Decision Tree Classifier
dt_model = DecisionTreeClassifier(class_weight='balanced', random_state=42)
dt_model.fit(X_train, y_train)
print("\nDecision Tree Confusion Matrix:")
print(confusion_matrix(y_test, dt_model.predict(X_test)))
print("\nDecision Tree Evaluation:")
print(classification_report(y_test, dt_model.predict(X_test)))

# XGBoost Classifier
xgb_model = XGBClassifier(objective='binary:logistic', eval_metric='logloss', use_label_encoder=False)
xgb_model.fit(X_train, y_train)
print("\nXGBoost Confusion Matrix:")
print(confusion_matrix(y_test, xgb_model.predict(X_test)))
print("\nXGBoost Evaluation:")
print(classification_report(y_test, xgb_model.predict(X_test)))

# LightGBM Classifier
lgbm_model = LGBMClassifier()
lgbm_model.fit(X_train, y_train)
print("\nLightGBM Confusion Matrix:")
print(confusion_matrix(y_test, lgbm_model.predict(X_test)))
print("\nLightGBM Evaluation:")
print(classification_report(y_test, lgbm_model.predict(X_test)))


# CatBoost Classifier
cat_model = CatBoostClassifier(iterations=100, learning_rate=0.1, depth=3, verbose=False)
cat_model.fit(X_train, y_train)
print("\nCatBoost Confusion Matrix:")
print(confusion_matrix(y_test, cat_model.predict(X_test)))
print("\nCatBoost Evaluation:")
print(classification_report(y_test, cat_model.predict(X_test)))


# Combining selected models with a Voting Classifier for a robust prediction
ensemble = VotingClassifier(estimators=[
    ('lr', lr_model), # Logistic Regression
    ('rf', rf_model), # Random Forest
    ('lgbm', lgbm_model) # LightGBM
], voting='soft')
ensemble.fit(X_train, y_train)
print("\nEnsemble model Confusion Matrix:")
print(confusion_matrix(y_test, ensemble.predict(X_test)))
print("\nEnsemble model Evaluation:")
print(classification_report(y_test, ensemble.predict(X_test)))

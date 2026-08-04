import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from pathlib import Path
import joblib
import os

current_file_path = Path(__file__).resolve()
project_root = current_file_path.parent.parent

dataset_path = project_root / 'dataset' / 'heart_disease_dataset.xlsx'
data_frame = pd.read_excel(str(dataset_path))

data_frame['BloodPressure'] = data_frame['BloodPressure'].fillna(data_frame['BloodPressure'].mean())
data_frame['Cholesterol'] = data_frame['Cholesterol'].fillna(data_frame['Cholesterol'].mean())
data_frame['HeartRate'] = data_frame['HeartRate'].fillna(data_frame['HeartRate'].median())
data_frame['BMI'] = data_frame['BMI'].fillna(data_frame['BMI'].mean())
data_frame['Smoking'] = data_frame['Smoking'].fillna(data_frame['Smoking'].mode()[0])
data_frame['FamilyHistory'] = data_frame['FamilyHistory'].fillna(data_frame['FamilyHistory'].mode()[0])
data_frame['ExerciseHours'] = data_frame['ExerciseHours'].fillna(data_frame['ExerciseHours'].mean())

data_frame['Gender'] = data_frame['Gender'].map({'Male': 1, 'Female': 0})
data_frame['Smoking'] = data_frame['Smoking'].map({'Yes': 1, 'No': 0})
data_frame['FamilyHistory'] = data_frame['FamilyHistory'].map({'Yes': 1, 'No': 0})

X = data_frame[['Age','Gender','BloodPressure','Cholesterol','HeartRate','Smoking','ExerciseHours','BMI','FamilyHistory']]
Y = data_frame[['HeartDisease']]

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.25, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = LogisticRegression(max_iter=1000, random_state=42)
model.fit(X_train_scaled, y_train.values.ravel())

model_dir_heart = project_root / "model"
model_dir_heart.mkdir(parents=True, exist_ok=True)

model_path_heart = model_dir_heart / "model.pkl"
scaler_path = model_dir_heart / "scaler.pkl"
joblib.dump(model, str(model_path_heart))
joblib.dump(scaler, str(scaler_path))



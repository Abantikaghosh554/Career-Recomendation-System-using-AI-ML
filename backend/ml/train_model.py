import pandas as pd
import numpy as np

from sklearn.preprocessing import OneHotEncoder, MultiLabelBinarizer, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report


# Load the dataset
df = pd.read_excel("backend/ml/career_dataset_large.xlsx")


# Remove duplicate rows
df = df.drop_duplicates()


# Handle missing certifications
df["Certifications"] = df["Certifications"].fillna("No Certification")


# Encode categorical columns
categorical_columns = [
    "Education Level",
    "Specialization",
    "Certifications"
]

encoder = OneHotEncoder(
    handle_unknown="ignore",
    sparse_output=False
)

encoded_categorical = encoder.fit_transform(
    df[categorical_columns]
)


# Encode skills
mlb = MultiLabelBinarizer()

skills_data = df["Skills"].apply(
    lambda x: [skill.strip() for skill in x.split(",")]
)

encoded_skills = mlb.fit_transform(skills_data)


# Encode target
label_encoder = LabelEncoder()

y = label_encoder.fit_transform(
    df["Recommended Career"]
)


# Combine all features
X = np.hstack([
    encoded_categorical,
    encoded_skills,
    df[["CGPA/Percentage"]].values
])


print("Final feature matrix:")
print("X shape:", X.shape)


# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


print("\nTraining the ML model...")


# Create Random Forest model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)


# Train the model
model.fit(X_train, y_train)


print("Model training completed!")


# Make predictions
y_pred = model.predict(X_test)


# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:")
print(accuracy)


# Classification report
print("\nClassification Report:")
print(
    classification_report(
        y_test,
        y_pred,
        target_names=label_encoder.classes_
    )
)
import pandas as pd
import numpy as np
import joblib

from sklearn.preprocessing import OneHotEncoder, MultiLabelBinarizer, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report


# Load the original Excel dataset
df = pd.read_csv("ml/career_training_data.csv")

print("Dataset loaded successfully!")
print("Original dataset shape:", df.shape)


# Remove duplicate rows
df = df.drop_duplicates()


# Handle missing certifications
df["Certifications"] = df["Certifications"].fillna("No Certification")


print("\nDataset after preprocessing:")
print("Shape:", df.shape)


# --------------------------------------------------
# Encode categorical features
# --------------------------------------------------

categorical_columns = [
    "Education",
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

print("\nCategorical features encoded!")
print("Encoded shape:", encoded_categorical.shape)


# --------------------------------------------------
# Encode skills
# --------------------------------------------------

mlb = MultiLabelBinarizer()

skills_data = df["Skills"].apply(
    lambda x: [skill.strip() for skill in x.split(",")]
)

encoded_skills = mlb.fit_transform(skills_data)

print("\nSkills encoded!")
print("Skill columns:")
print(mlb.classes_)
print("Encoded skill shape:", encoded_skills.shape)


# --------------------------------------------------
# Encode target career
# --------------------------------------------------

label_encoder = LabelEncoder()

y = label_encoder.fit_transform(
    df["Recommended Career"]
)

print("\nCareer labels encoded!")
print("Career classes:")
print(label_encoder.classes_)


# --------------------------------------------------
# Combine all features
# --------------------------------------------------

X = np.hstack([
    encoded_categorical,
    encoded_skills,
    df[
        [
            "CGPA",
            "Problem Solving",
            "Communication"
        ]
    ].values
])

print("\nFinal feature matrix:")
print("X shape:", X.shape)


# --------------------------------------------------
# Train-test split
# --------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("\nTrain-Test Split:")
print("X_train:", X_train.shape)
print("X_test:", X_test.shape)
print("y_train:", y_train.shape)
print("y_test:", y_test.shape)


# --------------------------------------------------
# Train Random Forest
# --------------------------------------------------

print("\nTraining Random Forest model...")

model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

model.fit(X_train, y_train)

print("Model training completed!")


# --------------------------------------------------
# Evaluate model
# --------------------------------------------------

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:")
print(f"{accuracy * 100:.2f}%")


print("\nClassification Report:")

print(
    classification_report(
        y_test,
        y_pred,
        target_names=label_encoder.classes_
    )
)


# --------------------------------------------------
# Save model and encoders
# --------------------------------------------------

print("\nSaving model and encoders...")

joblib.dump(
    model,
    "ml/career_model.pkl"
)

joblib.dump(
    encoder,
    "ml/categorical_encoder.pkl"
)

joblib.dump(
    mlb,
    "ml/skills_encoder.pkl"
)

joblib.dump(
    label_encoder,
    "ml/career_label_encoder.pkl"
)


print("\nAll files saved successfully!")

print("Created/updated files:")
print("career_model.pkl")
print("categorical_encoder.pkl")
print("skills_encoder.pkl")
print("career_label_encoder.pkl")
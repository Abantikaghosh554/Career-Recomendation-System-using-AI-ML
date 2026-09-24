import pandas as pd
import numpy as np
import joblib
import os

from sklearn.preprocessing import OneHotEncoder, MultiLabelBinarizer, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report


# ============================================================
# 1. Load training dataset
# ============================================================

df = pd.read_csv("backend/ml/career_training_data.csv")

print("Dataset loaded successfully!")
print("Dataset shape:", df.shape)


# ============================================================
# 2. Encode categorical features
# ============================================================

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


# ============================================================
# 3. Encode skills
# ============================================================

mlb = MultiLabelBinarizer()

skills_data = df["Skills"].apply(
    lambda x: [skill.strip() for skill in x.split(",")]
)

encoded_skills = mlb.fit_transform(skills_data)

print("\nSkills encoded!")
print("Skill columns:")
print(mlb.classes_)

print("Encoded skill shape:", encoded_skills.shape)


# ============================================================
# 4. Encode target career
# ============================================================

label_encoder = LabelEncoder()

y = label_encoder.fit_transform(
    df["Recommended Career"]
)

print("\nCareer labels encoded!")

print("Career classes:")
print(label_encoder.classes_)


# ============================================================
# 5. Combine all features
# ============================================================

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


# ============================================================
# 6. Split dataset
# ============================================================

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


# ============================================================
# 7. Create Random Forest model
# ============================================================

model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)


# ============================================================
# 8. Train model
# ============================================================

print("\nTraining final ML model...")

model.fit(
    X_train,
    y_train
)

print("Model training completed!")


# ============================================================
# 9. Make predictions
# ============================================================

y_pred = model.predict(X_test)


# ============================================================
# 10. Calculate accuracy
# ============================================================

accuracy = accuracy_score(
    y_test,
    y_pred
)

print("\nModel Accuracy:")
print(f"{accuracy * 100:.2f}%")


# ============================================================
# 11. Classification report
# ============================================================

print("\nClassification Report:")

print(
    classification_report(
        y_test,
        y_pred,
        target_names=label_encoder.classes_
    )
)


# ============================================================
# 12. Save model and encoders
# ============================================================

print("\nSaving model and encoders...")


# Create paths inside backend/ml
ml_folder = "backend/ml"

os.makedirs(ml_folder, exist_ok=True)


# Save Random Forest model
joblib.dump(
    model,
    os.path.join(ml_folder, "career_model.pkl")
)


# Save categorical encoder
joblib.dump(
    encoder,
    os.path.join(ml_folder, "categorical_encoder.pkl")
)


# Save skills encoder
joblib.dump(
    mlb,
    os.path.join(ml_folder, "skills_encoder.pkl")
)


# Save career label encoder
joblib.dump(
    label_encoder,
    os.path.join(ml_folder, "career_label_encoder.pkl")
)


print("\nAll files saved successfully!")

print("Created files:")
print("career_model.pkl")
print("categorical_encoder.pkl")
print("skills_encoder.pkl")
print("career_label_encoder.pkl")
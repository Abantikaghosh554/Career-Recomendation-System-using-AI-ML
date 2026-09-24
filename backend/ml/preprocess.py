import pandas as pd
import numpy as np

from sklearn.preprocessing import OneHotEncoder, MultiLabelBinarizer, LabelEncoder
from sklearn.model_selection import train_test_split


# Load the dataset
df = pd.read_excel("backend/ml/career_dataset_large.xlsx")


# Remove duplicate rows
df = df.drop_duplicates()


# Handle missing certifications
df["Certifications"] = df["Certifications"].fillna("No Certification")


print("Dataset after preprocessing:")
print(df.head())


print("\nDataset Shape:")
print(df.shape)


print("\nMissing Values:")
print(df.isnull().sum())


print("\nDuplicate Rows:")
print(df.duplicated().sum())


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

print("\nCategorical data encoded successfully!")
print("Encoded shape:", encoded_categorical.shape)


# Encode skills
mlb = MultiLabelBinarizer()

skills_data = df["Skills"].apply(
    lambda x: [skill.strip() for skill in x.split(",")]
)

encoded_skills = mlb.fit_transform(skills_data)

print("\nSkills encoded successfully!")
print("Skill columns:")
print(mlb.classes_)
print("Encoded skills shape:", encoded_skills.shape)


# Encode the target column
label_encoder = LabelEncoder()

y = label_encoder.fit_transform(
    df["Recommended Career"]
)

print("\nCareer target encoded successfully!")
print("Career classes:")
print(label_encoder.classes_)
print("Target shape:", y.shape)


# Combine all input features
X = np.hstack([
    encoded_categorical,
    encoded_skills,
    df[["CGPA/Percentage"]].values
])

print("\nFinal feature matrix:")
print("X shape:", X.shape)


# Split data into training and testing sets
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
import pandas as pd
import numpy as np
import joblib


# ============================================================
# 1. Load trained model and encoders
# ============================================================

model = joblib.load(
    "ml/career_model.pkl"
)

categorical_encoder = joblib.load(
    "ml/categorical_encoder.pkl"
)

skills_encoder = joblib.load(
    "ml/skills_encoder.pkl"
)

career_label_encoder = joblib.load(
    "ml/career_label_encoder.pkl"
)


print("Model and encoders loaded successfully!")


# ============================================================
# 2. Prediction function
# ============================================================

def predict_career(student):

    # Convert student information into DataFrame
    student_df = pd.DataFrame([student])


    # ========================================================
    # 3. Encode categorical features
    # ========================================================

    categorical_columns = [
        "Education",
        "Specialization",
        "Certifications"
    ]

    encoded_categorical = categorical_encoder.transform(
        student_df[categorical_columns]
    )


    # ========================================================
    # 4. Encode skills
    # ========================================================

    skills_data = student_df["Skills"].apply(
        lambda x: [skill.strip() for skill in x.split(",")]
    )

    encoded_skills = skills_encoder.transform(
        skills_data
    )


    # ========================================================
    # 5. Combine all features
    # ========================================================

    X_new = np.hstack([
        encoded_categorical,
        encoded_skills,
        student_df[
            [
                "CGPA",
                "Problem Solving",
                "Communication"
            ]
        ].values
    ])


    # ========================================================
    # 6. Predict career
    # ========================================================

    prediction = model.predict(X_new)


    # ========================================================
    # 7. Convert predicted number into career name
    # ========================================================

    predicted_career = career_label_encoder.inverse_transform(
        prediction
    )


    # ========================================================
    # 8. Return career name
    # ========================================================

    return predicted_career[0]
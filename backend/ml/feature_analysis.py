import pandas as pd

# Load the current career training dataset
df = pd.read_csv("ml/career_training_data.csv")

# Remove duplicate rows for analysis
df = df.drop_duplicates()

# Handle missing certifications
df["Certifications"] = df["Certifications"].fillna("No Certification")

print("Dataset shape after preprocessing:")
print(df.shape)

# 1. Education vs Career

print("\nEducation vs Recommended Career:")

education_career = pd.crosstab(
    df["Education"],
    df["Recommended Career"]
)

print(education_career)

# 2. Specialization vs Career

print("\nSpecialization vs Recommended Career:")

specialization_career = pd.crosstab(
    df["Specialization"],
    df["Recommended Career"]
)

print(specialization_career)

# 3. Certification vs Career

print("\nCertification vs Recommended Career:")

certification_career = pd.crosstab(
    df["Certifications"],
    df["Recommended Career"]
)

print(certification_career)

# 4. Skill vs Career

print("\nSkill vs Recommended Career:")

skills = [
    "Accounting",
    "Communication",
    "Counseling",
    "Data Analysis",
    "Financial Analysis",
    "MS Office",
    "Machine Learning",
    "Marketing",
    "Python",
    "SQL",
    "Excel",
    "Research"
]

for skill in skills:

    skill_data = df[
        df["Skills"].str.contains(
            skill,
            case=False,
            na=False
        )
    ]

    print(f"\n{skill}:")
    print(
        skill_data["Recommended Career"].value_counts()
    )

# 5. Average CGPA by Career

print("\nAverage CGPA by Career:")

average_cgpa = df.groupby(
    "Recommended Career"
)["CGPA"].mean().sort_values(
    ascending=False
)

print(average_cgpa)

# 6. Average Problem Solving by Career

print("\nAverage Problem Solving by Career:")

average_problem_solving = df.groupby(
    "Recommended Career"
)["Problem Solving"].mean().sort_values(
    ascending=False
)

print(average_problem_solving)

# 7. Average Communication by Career

print("\nAverage Communication by Career:")

average_communication = df.groupby(
    "Recommended Career"
)["Communication"].mean().sort_values(
    ascending=False
)

print(average_communication)

print("\nSample of complete records:")

print(
    df[
        [
            "Education",
            "Specialization",
            "Skills",
            "Certifications",
            "CGPA",
            "Problem Solving",
            "Communication",
            "Recommended Career"
        ]
    ].sample(
        min(20, len(df)),
        random_state=42
    ).to_string(index=False)
)
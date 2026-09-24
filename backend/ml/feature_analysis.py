import pandas as pd


# Load dataset
df = pd.read_excel("backend/ml/career_dataset_large.xlsx")


# Remove duplicate rows
df = df.drop_duplicates()


# Handle missing certifications
df["Certifications"] = df["Certifications"].fillna("No Certification")


print("Dataset shape:")
print(df.shape)

# 1. Education Level vs Career

print("\nEducation Level vs Recommended Career:")

education_career = pd.crosstab(
    df["Education Level"],
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
    "SQL"
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
        skill_data["Recommended Career"]
        .value_counts()
    )



# 5. Average CGPA by Career

print("\nAverage CGPA by Career:")

average_cgpa = df.groupby(
    "Recommended Career"
)["CGPA/Percentage"].mean().sort_values(
    ascending=False
)

print(average_cgpa)

print("\nSample of complete records:")

print(
    df[
        [
            "Education Level",
            "Specialization",
            "Skills",
            "Certifications",
            "CGPA/Percentage",
            "Recommended Career"
        ]
    ].sample(20, random_state=42).to_string(index=False)
)
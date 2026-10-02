import pandas as pd

# Load the current career training dataset
df = pd.read_csv("ml/career_training_data.csv")

print("Dataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nFirst 5 Rows:")
print(df.head().to_string(index=False))

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nCareer Counts:")
print(df["Recommended Career"].value_counts())

print("\nEducation Levels:")
print(df["Education"].value_counts())

print("\nSpecializations:")
print(df["Specialization"].value_counts())

print("\nCertifications:")
print(df["Certifications"].value_counts(dropna=False))

print("\nCGPA Range:")
print(df["CGPA"].describe())

print("\nSkills:")
print(df["Skills"].value_counts().head(30))

print("\nAll Individual Skills:")

all_skills = set()

for skill_list in df["Skills"]:
    skills = skill_list.split(",")

    for skill in skills:
        all_skills.add(skill.strip())

print(sorted(all_skills))
print("Total unique skills:", len(all_skills))
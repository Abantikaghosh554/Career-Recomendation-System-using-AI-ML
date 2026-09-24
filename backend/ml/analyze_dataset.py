import pandas as pd

df = pd.read_excel("backend/ml/career_dataset_large.xlsx")
print("Dataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nFirst 5 Rows:")
print(df.head())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nCareer Counts:")
print(df["Recommended Career"].value_counts())


print("\nEducation Levels:")
print(df["Education Level"].value_counts())

print("\nSpecializations:")
print(df["Specialization"].value_counts())

print("\nCertifications:")
print(df["Certifications"].value_counts(dropna=False))

print("\nCGPA/Percentage Range:")
print(df["CGPA/Percentage"].describe())

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
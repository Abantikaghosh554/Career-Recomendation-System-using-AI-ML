import pandas as pd


# Career profiles
career_profiles = {

    "Software Engineer": {
        "Education": "Bachelor's",
        "Specialization": "Computer Science",
        "Skills": "Python, SQL, Machine Learning",
        "Certifications": "AWS Certified"
    },

    "ML Engineer": {
        "Education": "Master's",
        "Specialization": "Computer Science",
        "Skills": "Python, Machine Learning, SQL",
        "Certifications": "AWS Certified"
    },

    "Data Scientist": {
        "Education": "Master's",
        "Specialization": "Computer Science",
        "Skills": "Python, Machine Learning, Data Analysis",
        "Certifications": "Google Data Analytics"
    },

    "Data Analyst": {
        "Education": "Bachelor's",
        "Specialization": "Commerce",
        "Skills": "Python, SQL, Data Analysis",
        "Certifications": "Google Data Analytics"
    },

    "Business Analyst": {
        "Education": "Bachelor's",
        "Specialization": "Business",
        "Skills": "Data Analysis, Communication, MS Office",
        "Certifications": "Google Data Analytics"
    },

    "Financial Analyst": {
        "Education": "Bachelor's",
        "Specialization": "Finance",
        "Skills": "Financial Analysis, Accounting, Excel",
        "Certifications": "CFA Level 1"
    },

    "Junior Accountant": {
        "Education": "Bachelor's",
        "Specialization": "Commerce",
        "Skills": "Accounting, Financial Analysis, MS Office",
        "Certifications": "Tally ERP"
    },

    "Marketing Executive": {
        "Education": "Bachelor's",
        "Specialization": "Business",
        "Skills": "Marketing, Communication, MS Office",
        "Certifications": "Digital Marketing"
    },

    "Sales Assistant": {
        "Education": "Intermediate",
        "Specialization": "Business",
        "Skills": "Communication, Marketing, MS Office",
        "Certifications": "Digital Marketing"
    },

    "School Counselor": {
        "Education": "Master's",
        "Specialization": "Psychology",
        "Skills": "Counseling, Communication",
        "Certifications": "Mental Health Basics"
    },

    "Professor": {
        "Education": "PhD",
        "Specialization": "Science",
        "Skills": "Communication, Research",
        "Certifications": "No Certification"
    },

    "Research Scientist": {
        "Education": "PhD",
        "Specialization": "Science",
        "Skills": "Machine Learning, Data Analysis, Python",
        "Certifications": "No Certification"
    },

    "Clerk": {
        "Education": "Intermediate",
        "Specialization": "Commerce",
        "Skills": "MS Office, Communication",
        "Certifications": "Tally ERP"
    },

    "Data Entry Operator": {
        "Education": "Intermediate",
        "Specialization": "Commerce",
        "Skills": "MS Office, Communication",
        "Certifications": "No Certification"
    }
}


# Convert dictionary to DataFrame
df = pd.DataFrame.from_dict(
    career_profiles,
    orient="index"
)

df.index.name = "Recommended Career"

df.reset_index(inplace=True)


# Display dataset
print("Career Profile Dataset:")
print(df.to_string(index=False))


print("\nDataset Shape:")
print(df.shape)


# Save dataset
df.to_csv(
    "career_profiles.csv",
    index=False
)

print("\ncareer_profiles.csv created successfully!")

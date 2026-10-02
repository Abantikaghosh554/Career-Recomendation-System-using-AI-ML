import pandas as pd
import random


# Load career profiles
df = pd.read_csv("ml/career_profiles.csv")


# Number of students to generate for each career
samples_per_career = 300


training_data = []


for _, career in df.iterrows():

    for _ in range(samples_per_career):

        # Generate a CGPA between 6.0 and 10.0
        cgpa = round(random.uniform(6.0, 10.0), 2)

        # Generate problem-solving and communication scores
        problem_solving = random.randint(5, 10)
        communication = random.randint(5, 10)

        training_data.append({

            "Education": career["Education"],

            "Specialization": career["Specialization"],

            "Skills": career["Skills"],

            "Certifications": career["Certifications"],

            "CGPA": cgpa,

            "Problem Solving": problem_solving,

            "Communication": communication,

            "Recommended Career": career["Recommended Career"]
        })


# Convert to DataFrame
training_df = pd.DataFrame(training_data)


# Shuffle the dataset
training_df = training_df.sample(
    frac=1,
    random_state=42
).reset_index(drop=True)


# Save dataset
training_df.to_csv(
    "ml/career_training_data.csv",
    index=False
)


print("Training dataset created successfully!")

print("\nDataset shape:")
print(training_df.shape)

print("\nFirst 10 rows:")
print(training_df.head(10).to_string(index=False))

print("\nCareer distribution:")
print(training_df["Recommended Career"].value_counts())
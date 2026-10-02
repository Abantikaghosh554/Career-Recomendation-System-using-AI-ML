import pandas as pd


# Load the career profile dataset
df = pd.read_csv("ml/career_profiles.csv")


print("Career Profile Dataset:")
print(df.to_string(index=False))


print("\nDataset Shape:")
print(df.shape)


print("\nMissing Values:")
print(df.isnull().sum())


print("\nDuplicate Rows:")
print(df.duplicated().sum())
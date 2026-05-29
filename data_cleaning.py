import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("netflix_titles.csv")

# Display first 5 rows
print("\nFIRST 5 ROWS:")
print(df.head())

# Display dataset information
print("\nDATASET INFO:")
print(df.info())

# Check missing values
print("\nMISSING VALUES:")
print(df.isnull().sum())

# Fill missing values
df['director'] = df['director'].fillna('Unknown')
df['cast'] = df['cast'].fillna('Not Available')
df['country'] = df['country'].fillna('Unknown')
df['rating'] = df['rating'].fillna('Not Rated')

# Remove duplicate rows
duplicates = df.duplicated().sum()
print("\nDUPLICATE ROWS:", duplicates)

df = df.drop_duplicates()

# Clean column names
df.columns = df.columns.str.lower().str.replace(' ', '_')

# Convert date column
df['date_added'] = pd.to_datetime(df['date_added'].str.strip(), errors='coerce')
# Standardize text values
df['type'] = df['type'].str.lower()
df['country'] = df['country'].str.strip()

# Final dataset info
print("\nFINAL DATASET INFO:")
print(df.info())

# Save cleaned dataset
df.to_csv("cleaned_netflix_dataset.csv", index=False)

print("\nData Cleaning Completed Successfully!")
print("Cleaned dataset saved as cleaned_netflix_dataset.csv")
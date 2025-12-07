import pandas as pd
import io
import os


csv_data = """Name,Age,City,Score
Alice,24,New York,85.5
Bob,27,London,72.1
Charlie,22,Paris,91.8
David,32,New York,65.3
Eve,29,London,88.9
Frank,25,Paris,79.0
"""
FILE_NAME = "mock_students.csv"


with open(FILE_NAME, 'w') as f:
    f.write(csv_data)


print("--- 1. Loading CSV File ---")
df = pd.read_csv(FILE_NAME)
print("Original DataFrame:")
print(df)


print("\n--- 2. Filtering (Age > 25) ---")
filtered_df = df[df['Age'] > 25]
print(filtered_df)

print("\n--- 3. Sorting (by Score, descending) ---")
sorted_df = df.sort_values(by='Score', ascending=False)
print(sorted_df)


print("\n--- 4. Summary Statistics for 'Age' and 'Score' ---")

summary_stats = df[['Age', 'Score']].describe()
print(summary_stats)

print("\nMean Score:", df['Score'].mean())
print("Count of students in each City:")
print(df['City'].value_counts())


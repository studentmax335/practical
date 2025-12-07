import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# Set a style for better visualization
sns.set_theme(style="whitegrid")

# 1. Prepare Data
# Create a sample DataFrame
np.random.seed(42)
data = {
    'Exam_Score': np.random.normal(75, 10, 100), # Mean 75, Std Dev 10
    'Study_Hours': np.random.uniform(5, 30, 100),
    'Pass_Status': np.random.choice(['Pass', 'Fail'], 100, p=[0.7, 0.3])
}
df = pd.DataFrame(data)

# --- 1. Histogram (Using Matplotlib and Seaborn) ---

plt.figure(figsize=(12, 5))

# Subplot 1: Matplotlib Histogram
plt.subplot(1, 2, 1)
plt.hist(df['Exam_Score'], bins=10, color='skyblue', edgecolor='black', alpha=0.7)
plt.title('Exam Score Distribution (Matplotlib Hist)')
plt.xlabel('Exam Score')
plt.ylabel('Frequency')

# Subplot 2: Seaborn Distribution Plot (KDE is optional but good practice)
plt.subplot(1, 2, 2)
sns.histplot(df, x='Exam_Score', kde=True, bins=10, color='teal')
plt.title('Exam Score Distribution (Seaborn Histplot)')
plt.xlabel('Exam Score')
plt.ylabel('Density/Count')

plt.tight_layout()
plt.show()

# --- 2. Scatter Plot (Using Seaborn and Matplotlib) ---

plt.figure(figsize=(12, 5))

# Subplot 3: Matplotlib Scatter Plot
plt.subplot(1, 2, 1)
plt.scatter(df['Study_Hours'], df['Exam_Score'], 
            c='red', # color
            marker='x', # marker shape
            label='Scores')
plt.title('Study Hours vs. Exam Score (Matplotlib Scatter)')
plt.xlabel('Study Hours')
plt.ylabel('Exam Score')
plt.legend()

# Subplot 4: Seaborn Scatter Plot (with additional dimension 'hue')
plt.subplot(1, 2, 2)
sns.scatterplot(data=df, x='Study_Hours', y='Exam_Score', 
                hue='Pass_Status', # Color points based on Pass/Fail
                style='Pass_Status', # Change marker style based on Pass/Fail
                palette={'Pass': 'green', 'Fail': 'red'},
                s=100) # Size of the points
plt.title('Study Hours vs. Exam Score (Seaborn Scatter)')
plt.xlabel('Study Hours')
plt.ylabel('Exam Score')

plt.tight_layout()
plt.show()

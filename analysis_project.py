# Student Data Analysis Project

print("PROJECT STARTED")


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('ggplot')

# Load dataset
df = pd.read_csv("data/StudentsPerformance.csv")

df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

print("Columns after cleaning:", df.columns)

# Basic Exploration

print("\nFirst 5 Rows:\n")
print(df.head())

print("\nDataset Info:\n")
print(df.info())

print("\nStatistical Summary:\n")
print(df.describe())

# Data Analysis

math_avg = df['math_score'].mean()
reading_avg = df['reading_score'].mean()
writing_avg = df['writing_score'].mean()

print("\nAverage Scores:")
print("Math:", math_avg)
print("Reading:", reading_avg)
print("Writing:", writing_avg)

# Visualization 1 — Bar Chart

subjects = ['Math', 'Reading', 'Writing']
averages = [math_avg, reading_avg, writing_avg]

plt.figure(figsize=(8,5))
plt.bar(subjects, averages)
plt.title("Average Score by Subject")
plt.xlabel("Subjects")
plt.ylabel("Average Score")

plt.savefig("images/bar_chart.png")
plt.show()

# Visualization 2 — Scatter Plot

plt.figure(figsize=(8,5))
plt.scatter(df['math_score'], df['reading_score'])
plt.xlabel("Math Score")
plt.ylabel("Reading Score")
plt.title("Math vs Reading Scores")

plt.savefig("images/scatter_plot.png")
plt.show()

# Visualization 3 — Heatmap

plt.figure(figsize=(8,6))
correlation = df[['math_score','reading_score','writing_score']].corr()

sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title("Score Correlation Heatmap")

plt.savefig("images/heatmap.png")
plt.show()

print("\nINSIGHTS:")
print(" Students perform similarly in reading and writing.")
print(" Reading and writing show strong correlation.")
print(" Math scores are slightly lower on average.")
print(" Students strong in one subject tend to perform well in others.")


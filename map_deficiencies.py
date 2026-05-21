import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
print("Loading Micronutrient Deficiency Data...")
df = pd.read_csv("deficiency_data.csv")

# 1. Analyze Average Micronutrient Levels by Region
print("\n--- Regional Disparities ---")
regional_analysis = df.groupby('Region')[['Iron_Level_mg_dL', 'VitaminD_Level_ng_mL']].mean().reset_index()
print(regional_analysis)

# 2. Visualize Iron Levels across Age Groups
plt.figure(figsize=(8, 5))
sns.boxplot(x='Age_Group', y='Iron_Level_mg_dL', hue='Gender', data=df, palette='Set2')
plt.title('Iron Levels Distribution by Age Group and Gender')
plt.ylabel('Iron Level (mg/dL)')
plt.xlabel('Age Group')
plt.savefig('iron_distribution.png')
print("Saved plot: iron_distribution.png")

# 3. Categorize Deficiency Status
plt.figure(figsize=(7, 5))
sns.countplot(x='Deficiency_Status', data=df, order=['None', 'Low', 'Moderate', 'High'], palette='Reds')
plt.title('Count of Patients by Deficiency Severity')
plt.savefig('deficiency_severity.png')
print("Saved plot: deficiency_severity.png")

print("\nAnalysis complete. Check generated PNG files.")

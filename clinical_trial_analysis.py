
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Sample clinical trials dropout dataset
data = {
    'Patient_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Trial_Phase': ['Phase 1', 'Phase 2', 'Phase 1', 'Phase 2', 'Phase 1', 'Phase 1', 'Phase 2', 'Phase 1', 'Phase 2', 'Phase 1'],
    'Dropout': ['Yes', 'No', 'No', 'Yes', 'Yes', 'No', 'Yes', 'No', 'No', 'Yes'],
    'Age': [34, 28, 45, 36, 38, 50, 42, 29, 33, 39],
    'Gender': ['Male', 'Female', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Male', 'Female']
}

# Creating a DataFrame
df = pd.DataFrame(data)

# Convert 'Dropout' column to binary
df['Dropout'] = df['Dropout'].map({'Yes': 1, 'No': 0})

# Summary statistics
print("Summary Statistics:")
print(df.describe())

# Dropout distribution
sns.countplot(x='Dropout', data=df)
plt.title('Dropout Distribution')
plt.xlabel('Dropout (1 = Yes, 0 = No)')
plt.ylabel('Count')
plt.show()

# Age vs Dropout boxplot
sns.boxplot(x='Dropout', y='Age', data=df)
plt.title('Age vs Dropout')
plt.xlabel('Dropout (1 = Yes, 0 = No)')
plt.ylabel('Age')
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your 'sample_data.csv' file
df = pd.read_csv('sample_data.csv')


plt.figure(figsize=(6,4))
sns.countplot(x='Gender',data = df, palette ='pastel')
plt.title('Distribution of Genders')
plt.xlabel('count')
plt.ylabel('count')
plt.show()

plt.figure(figsize=(6,4))
sns.histplot(df['Age'], bins = 5, kde=True, color='skyblue')
plt.title('Distribution of Age')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(7,4))
sns.histplot(data=df, x='Age', hue='Gender',bins =5, kde=True, palette='Set2',alpha=0.7)
plt.title('Distribution of Age by Gender')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

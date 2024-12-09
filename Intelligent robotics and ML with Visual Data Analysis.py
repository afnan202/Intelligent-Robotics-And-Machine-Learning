import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
from sklearn.preprocessing import StandardScaler
sns.set()
plt.rcParams['figure.figsize'] = (10, 6)

# Load the data
df = pd.read_csv("telecom_churn.csv")
print("Data Loaded:\n", df.head())

# 1. Univariate Analysis
# Histogram
df['Total day minutes'].hist(bins=20, color='skyblue', edgecolor='black')
plt.title("Histogram of Total Day Minutes")
plt.xlabel("Minutes")
plt.ylabel("Frequency")
plt.show()
# Density Plot
sns.histplot(df['Total day minutes'], kde=True)
plt.title("Density Plot of Total Day Minutes")
plt.show()
# Box Plot
sns.boxplot(x=df['Total intl calls'])
plt.title("Box Plot of Total Intl Calls")
plt.show()
# Violin Plot
sns.violinplot(x=df['Total intl calls'])
plt.title("Violin Plot of Total Intl Calls")
plt.show()
print("Descriptive Statistics:\n", df[['Total day minutes', 'Total intl calls']].describe())
# Categorical Features
# Frequency Table
print("Frequency Table:\n", df['Churn'].value_counts())
# Bar Plot
sns.countplot(x="Churn", data=df)
plt.title("Bar Plot of Churn")
plt.show()
# 2. Multivariate Analysis
# Correlation Matrix
corr_matrix = df.corr()
sns.heatmap(corr_matrix, annot=True, fmt='.2f', cmap='coolwarm')
plt.title("Correlation Matrix")
plt.show()
# Scatter Plot
sns.scatterplot(x='Total day minutes', y='Total night minutes', data=df, hue='Churn')
plt.title("Scatter Plot of Total Day vs Night Minutes")
plt.show()
# 3. Exploring Relationships
# Box Plot by Categorical Variable
sns.boxplot(x='Churn', y='Total day minutes', data=df)
plt.title("Box Plot of Total Day Minutes by Churn")
plt.show()
# Categorical vs Categorical
sns.countplot(x='Customer service calls', hue='Churn', data=df)
plt.title("Count Plot of Customer Service Calls by Churn")
plt.show()

# 4. Whole Dataset Visualization 
# Scatterplot Matrix
sns.pairplot(df, diag_kind='kde', hue='Churn')
plt.suptitle("Scatterplot Matrix", y=1.02)
plt.show()
# t-SNE for Dimensionality Reduction
X = df.drop(['Churn', 'State'], axis=1)
X['International plan'] = X['International plan'].map({'Yes': 1, 'No': 0})
X['Voice mail plan'] = X['Voice mail plan'].map({'Yes': 1, 'No': 0})
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
tsne = TSNE(random_state=42)
tsne_repr = tsne.fit_transform(X_scaled)
plt.scatter(tsne_repr[:, 0], tsne_repr[:, 1], c=df['Churn'].map({False: 'blue', True: 'orange'}), alpha=0.5)
plt.title("t-SNE Visualization")
plt.xlabel("Dimension 1")
plt.ylabel("Dimension 2")
plt.show()

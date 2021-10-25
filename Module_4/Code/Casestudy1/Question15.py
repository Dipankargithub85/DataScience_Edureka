import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm
import seaborn as sns

# Phase 1 - Data Collection
df_school_data = pd.read_csv("middle_tn_schools.csv")
print(df_school_data.describe())

#Phase 2 - Group data by school ratings
df_grouped_data = df_school_data.groupby("school_rating").describe()
print(df_grouped_data.head())

# Phase 3 –Correlation analysis
corrmat = df_grouped_data.corr()
print(corrmat)
f, ax = plt.subplots(figsize=(9, 8))
sns.heatmap(corrmat, ax=ax, cmap="YlGnBu", linewidths=0.1)

#Phase 4 – Scatter Plot
plt.scatter(df_school_data["school_rating"], df_school_data["reduced_lunch"])
plt.grid()
plt.xlabel("Rating")
plt.ylabel("Reduced lunch")
plt.title("School rating vs Reduced lunch")
plt.show()

#Phase 5 – Correlation Matrix
corr = df_school_data.corr()
fig, ax = plt.subplots(figsize=(15, 15))
ax.matshow(corr)
plt.xticks(range(len(corr.columns)), corr.columns)
plt.yticks(range(len(corr.columns)), corr.columns)



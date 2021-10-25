import pandas as pd

df = pd.read_csv('D:\\work\\Python\\python_for_edureka_doc\\Module_5\\574_m5_datasets_v3.0\\HollywoodMovies.csv')

sorted_df = df.sort_values("Budget", ascending=False)

sorted_df = sorted_df[sorted_df["Budget"] > 0]  # removing nan values

print(sorted_df.head(5))
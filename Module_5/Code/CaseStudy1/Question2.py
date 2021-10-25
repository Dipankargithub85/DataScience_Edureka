import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('D:\\work\\Python\\python_for_edureka_doc\\Module_5\\574_m5_datasets_v3.0\\HollywoodMovies.csv')

genre_groups = df.groupby("Genre").groups

genre_groups.keys()

plt.bar(genre_groups.keys(), [len(values) for values in genre_groups.values()])
plt.xlabel("Genre")
plt.ylabel("Number of movies")
plt.title("Genre vs Number of Movies")

plt.setp(plt.gca().get_xticklabels(), rotation=90,
         horizontalalignment='right')  # Rotate Axis Labels

plt.grid()
plt.show()
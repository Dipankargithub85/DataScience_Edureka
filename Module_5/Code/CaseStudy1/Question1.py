import pandas as pd

df = pd.read_csv('D:\\work\\Python\\python_for_edureka_doc\\Module_5\\574_m5_datasets_v3.0\\HollywoodMovies.csv')

highest_rate = df[df["Story"] == "Quest"]["RottenTomatoes"].max()

highest_rated_movies = df[df["RottenTomatoes"] == highest_rate]

print(highest_rated_movies)
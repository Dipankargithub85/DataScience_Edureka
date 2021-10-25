import pandas as pd

df_data_file = pd.read_csv("data_file.txt")
df_data_file.to_csv("data_file.csv")
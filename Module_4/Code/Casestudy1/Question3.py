import pandas as pd

df = pd.read_csv("D:\\work\\Python\\python_for_edureka_doc\\Module_4\\574_m4_datasets_v3.0\\SalaryGender.csv")
values = df[df.PhD ==1]
print(values)
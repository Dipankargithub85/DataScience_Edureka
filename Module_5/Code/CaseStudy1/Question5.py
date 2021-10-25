import pandas as pd

# 5.1
df = pd.DataFrame({'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
                   'last_name': ['Miller', 'Jacobson', ".", 'Milner', 'Cooze'],
                   'age': [42, 52, 36, 24, 73],
                   'preTestScore': [4, 24, 31, ".", "."],
                   'postTestScore': ["25,000", "94,000", 57, 62, 70]})


# 5.2
df.to_csv("example.csv")
print("*"*20)

# 5.3
df = pd.read_csv("example.csv")
print(df)
print("*"*20)

# 5.4
df_without_header = pd.read_csv("example.csv", header=None)
print(df_without_header)
print("*"*20)

# 5.5
df_with_index = pd.read_csv("example.csv", index_col=[
                            "first_name", "last_name"])
print(df_with_index)
print("*"*20)

# 5.6
boolean_df = df.isnull().any()
print(boolean_df)
print("*"*20)

# 5.7
df_skip_rows = pd.read_csv("example.csv", skiprows=3)
print(df_skip_rows)
print("*"*20)
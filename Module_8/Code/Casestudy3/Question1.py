import pandas as pd
from sklearn.decomposition import PCA


# Data Collection
data = pd.read_csv("D:\\work\\Python\\python_for_edureka_doc\\Module_8\\breast-cancer-data.csv", index_col=0)
#print(data.head())
#print(data.columns)

# Data Wrangling
df= data['diagnosis']
df_cancer = data
#print(df_cancer.head())

df_cancer.drop(["diagnosis"], inplace=True, axis=1)
#print(df_cancer.head())
#print(data.columns)
#print(df.head())

# Data Transformation
model_pca = PCA(n_components = 2)
model_pca.fit(df_cancer)
transformer_data = model_pca.transform(df_cancer)


# New DataFrame
new_df = pd.DataFrame(transformer_data)
new_df.index = df_cancer.index # Setting original Index
new_df.columns = ["PC1", "PC2"] # Changing Column names
print("===================================")
print(new_df.head())
#print(df.columns)
new_df['diagnosis'] = df # Adding Result column
print(new_df.head())


#Variance Ratio
print(model_pca.explained_variance_ratio_)

from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
import pandas as pd


df_horse = pd.read_csv("D:\\work\\Python\\python_for_edureka_doc\\Module_7\\horse.csv")
df_horse.head()


# 1.Let’s attempt to predict the survival of a horse based on various observed medical conditions.

df_horse.isna()

Y = df_horse["outcome"]
X = df_horse.drop(["outcome"], axis=1)

# 2.This dataset contains many categorical features, replace them with label encoding.
X = pd.get_dummies(X)
X.head()

# 3.Replace the missing values by the most frequent value in each column.
X = X.apply(lambda x: x.fillna(x.value_counts().index[0]))


# 4.Fit a decision tree classifier and observe the accuracy.
dec_tree = DecisionTreeClassifier()
dec_tree.fit(X, Y)
predicted_outcome = dec_tree.predict(X)
print(metrics.accuracy_score(predicted_outcome, Y))

# 5.Fit a random forest classifier and observe the accuracy
random_forest = RandomForestClassifier()
random_forest.fit(X, Y)
predicted_outcome = random_forest.predict(X)
print(metrics.accuracy_score(predicted_outcome, Y))
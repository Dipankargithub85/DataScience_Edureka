import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics


data = pd.read_csv("D:\\work\\Python\\python_for_edureka_doc\\Module_9\\voice-classification.csv")
data.head()


X = data.iloc[:, :len(data.columns)-1]
Y = data["label"]

train_x, test_x, train_y, test_y = train_test_split(
    X, Y, random_state=10, test_size=0.30)

g_model = GaussianNB()
g_model.fit(train_x, train_y)

predicted_values = g_model.predict(test_x)
print(metrics.accuracy_score(predicted_values, test_y)*100)
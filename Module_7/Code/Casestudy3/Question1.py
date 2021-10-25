from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pandas as pd


# Data Collection
data = pd.read_csv("D:\\work\\Python\\python_for_edureka_doc\\Module_7\\loan_borowwer_data.csv")
#print(data.head())

# Data Wrangling
X = data.iloc[:, 2:13]
Y = data["not.fully.paid"]

# Split Data
train_x, test_x, train_y, test_y = train_test_split(
    X, Y, random_state=10, test_size=0.3)

# Model creation and Fitting Model
random_class = RandomForestClassifier()
random_class.fit(train_x, train_y)

# Data Prediction
predicted_values = random_class.predict(test_x)

# Check Accuracy Score
print(metrics.accuracy_score(predicted_values, test_y)*100)
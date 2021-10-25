from sklearn.preprocessing import StandardScaler
import pandas as pd
from sklearn.model_selection import train_test_split, ShuffleSplit, GridSearchCV
from sklearn import svm
from sklearn import metrics
from sklearn.preprocessing import LabelEncoder

# 1.Load the data from “college.csv” that has attributes collected about private and public colleges
# for a particular year. We will try to predict the private/public status of the college from other attributes.
data = pd.read_csv("D:\\work\\Python\\python_for_edureka_doc\\Module_9\\College.csv")
data.head()

labelencoder = LabelEncoder()
data["Private"] = labelencoder.fit_transform(data["Private"])
print(data.head())


# 2.Use LabelEncoder to encode the target variable in to numerical form and split the data such that 20% of the data is set aside fortesting.
X = data.iloc[:, 1:]
Y = data["Private"]

train_x, test_x, train_y, test_y = train_test_split(X, Y, test_size=0.30, random_state=10)


# 3.Fit a linear svm from scikit learn and observe the accuracy.[Hint:Use Linear SVC
model_svm = svm.LinearSVC()
model_svm.fit(train_x, train_y)
predicted_values = model_svm.predict(test_x)

print("Accuracy Score:-")
print(metrics.accuracy_score(predicted_values, test_y)*100)
print("============================================================================")


# 4.Preprocess the data using StandardScalar and fit the same model again and observe the change in accuracy.

scaler_df = StandardScaler().fit_transform(X)
scaler_df = pd.DataFrame(X, columns=X.columns)

X = scaler_df
Y = data["Private"]

train_x, test_x, train_y, test_y = train_test_split(
    X, Y, test_size=0.30, random_state=10)

model_svm = svm.LinearSVC()
model_svm.fit(train_x, train_y)

predicted_values = model_svm.predict(test_x)
print(metrics.accuracy_score(predicted_values, test_y)*100)
print("=========================================================================")
# 5.Use scikit learn’s gridsearch to select the best hyperparameter for a non-linear SVM,identify the model with
# best score and its parameters.

parameter_candidates = [
    {'C': [1, 10, 100, 1000], 'kernel': ['poly']},
    {'C': [1, 10, 100, 1000], 'kernel': ['linear']},
    {'C': [1, 10, 100, 1000], 'gamma': [0.001, 0.0001], 'kernel': ['rbf']},
]

# Create a classifier object with the classifier and parameter candidates
cv = ShuffleSplit()
clf = GridSearchCV(estimator=svm.SVC(max_iter=1000),
                   param_grid=parameter_candidates, n_jobs=-1, cv=cv)

# Train the classifier on data1's feature and target data
clf.fit(train_x, train_y)

# View the accuracy score
print('Best score for data1:', clf.best_score_)

# View the best parameters for the model found using grid search
print('Best C:', clf.best_estimator_.C)
print('Best Kernel:', clf.best_estimator_.kernel)
print('Best Gamma:', clf.best_estimator_.gamma)

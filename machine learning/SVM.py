import pandas as pd
from sklearn import preprocessing, cross_validation, neighbors, svm
import numpy as np
from sklearn.cross_validation import train_test_split
import pickle

df = pd.read_csv('C:\\Users\\Rakshith\\Desktop\\bco\\breast-cancer-wisconsin.data')
df.replace('?', -99999, inplace=True)
df.drop(['id'], 1,  inplace=True)

X = np.array(df.drop(["class"], 1))
y = np.array(df["class"])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
clf = svm.SVC()
clf.fit(X_train, y_train)


with open("SVM",'wb') as f:
    pickle.dump(clf, f)
pickle_in = open('SVM', 'rb')
clf = pickle.load(pickle_in)


accuracy = clf.score(X_test, y_test)
print(accuracy)

# example_measure = np.array([[4,2,1,1,1,2,3,2,1],[4,2,1,1,1,2,3,2,1]])
# example_measure = example_measure.reshape(len(example_measure), -1)
# prediction = clf.predict(example_measure)
# print(prediction)

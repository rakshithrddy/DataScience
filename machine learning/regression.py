import pandas as pd
import quandl, math, datetime
import numpy as np
from sklearn import preprocessing, svm
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from matplotlib import style
import pickle

style.use('ggplot')

pd.set_option("display.max_columns", 12)

df = quandl.get('WIKI/GOOGL')
# print(df.head())
df = df[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume']]
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Close']) / df['Adj. Close'] * 100.0   # high - close(highest tat day) div close
df['PTC_CHANGE'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0   # highest(that day) - lowest(that day) div lowest

df = df[['Adj. Close', 'HL_PCT', 'PTC_CHANGE', 'Adj. Volume']]  # features

forecast_col = 'Adj. Close'
df.fillna(-99999, inplace=True)

forecast_out = int(math.ceil(0.1*len(df)))
print(forecast_out)
df['label'] = df[forecast_col].shift(-forecast_out)  # labels


X = np.array(df.drop(['label'], 1))  # features are X
X = preprocessing.scale(X)
X_lately = X[:-forecast_out:]
X = X[:-forecast_out]

df.dropna(inplace=True)
y = np.array(df['label'])     # labels are y

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

clf = LinearRegression(n_jobs=-1)  # classifier  # n_jobs is the number of threads run in parallel -1 = max number by the cpu
clf.fit(X_train, y_train)
with open('linearregression','wb') as f:  #opeaning a file with pickle and saving the model
    pickle.dump(clf, f)

pickle_in = open('linearregression','rb')   #reading the model from the file
clf = pickle.load(pickle_in)

clf.score(X_train, y_train)
accuracy = clf.score(X_train, y_train)

forecast_set = clf.predict(X_lately)
print(forecast_set, accuracy, forecast_out)

df['Forecast'] = np.nan

last_date = df.iloc[-1].name
last_unix = last_date.timestamp()
one_day = 86400
next_unix = last_unix + one_day

for i in forecast_set:
    next_date = datetime.datetime.fromtimestamp(next_unix)
    next_unix += one_day
    df.loc[next_date] = [np.nan for _ in range(len(df.columns)-1)] + [i]

df['Adj. Close'].plot()
df['Forecast'].plot()
plt.legend(loc=4)
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()
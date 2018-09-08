import datetime as dt
import pandas as pd
import pandas_datareader as web

start = dt.datetime(2017, 11, 1)
end = dt.datetime(2018, 1, 1)

tickers = ['NASDAQ:AAPL','NASDAQ:MSFT','NYSE:GE','NYSE:IBM','NYSE:AA','NYSE:DAL','NYSE:UAL', 'NYSE:PEP', 'NYSE:KO']
sp500 = web.DataReader(tickers, 'google', start, end)
print(sp500.head())

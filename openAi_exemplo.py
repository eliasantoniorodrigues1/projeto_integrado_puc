import numpy as np
import talib

# create a sample dataset
data = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

# calculate the moving average
ma = talib.MA(data, timeperiod=3)

# print the moving average
print(ma)



import yfinance as yf
import ta

# download the stock price data for Apple
apple = yf.Ticker("AAPL")
df = apple.history(period="1y")

# calculate the STOCHRSI indicator with a time period of 14 days
stochrsi = ta.momentum.STOCHRSIIndicator(df["Close"], window=14)

# add the STOCHRSI values to the DataFrame
df["STOCHRSI"] = stochrsi.stochrsi()

# print the DataFrame
print(df)



import yfinance as yf
import ta
import matplotlib.pyplot as plt

# download the stock price data for Apple
apple = yf.Ticker("AAPL")
df = apple.history(period="1y")

# calculate the STOCHRSI indicator with a time period of 14 days
stochrsi = ta.momentum.STOCHRSIIndicator(df["Close"], window=14)

# add the STOCHRSI values to the DataFrame
df["STOCHRSI"] = stochrsi.stochrsi()

# plot the closing prices and STOCHRSI values on a graph
plt.plot(df["Close"], label="Closing Price")
plt.plot(df["STOCHRSI"], label="STOCHRSI")
plt.legend()
plt.show()




import yfinance as yf
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR

# download stock price data for Apple
apple = yf.Ticker("AAPL")
df = apple.history(period="1y")

# prepare the data for SVM training
X = pd.DataFrame(index=df.index)
X["Close"] = df["Close"]
scaler = StandardScaler()
X = scaler.fit_transform(X)
y = X[1:]
X = X[:-1]

# split the data into training and testing sets
split = int(0.8 * len(X))
X_train, y_train, X_test, y_test = X[:split], y[:split], X[split:], y[split:]

# train the SVM model
svm = SVR(kernel="rbf", C=1e3, gamma=0.1)
svm.fit(X_train, y_train)

# make predictions on the test set
y_pred = svm.predict(X_test)

# evaluate the model's performance
mse = ((y_pred - y_test) ** 2).mean()
rmse = mse ** 0.5
print("Root Mean Squared Error:", rmse)

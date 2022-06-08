# Import necessary libraries
import yfinance as yf
import pandas as pd

# Import Freetrade stocks from CSV
freetrade = pd.read_csv('freetrade.csv')

# Isolate US-based stocks
us_df = freetrade.loc[freetrade['Currency'] == 'usd']
us_stocks = us_df['Symbol'].tolist()

# Download financial data from Yahoo Finance
df = yf.download(us_stocks, period="5y")
close = df['Close']
df.to_csv('price_data.csv', header=True)
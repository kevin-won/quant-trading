import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

start_date = "2020-01-01"
end_date = "2021-01-01"

pepsi = yf.download('PEP', start=start_date, end=end_date)
coke = yf.download('KO', start=start_date, end=end_date)

pepsi_close = pepsi['Close']
coke_close = coke['Close']

plt.figure(figsize=(12, 6))
plt.plot(pepsi_close, label='PepsiCo (PEP)', color='blue')
plt.plot(coke_close, label='Coca-Cola (KO)', color='red')
plt.title('Closing Prices of PepsiCo and Coca-Cola')
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.legend()
plt.show()

spread = pepsi_close - coke_close

plt.figure(figsize=(12, 6))
plt.plot(spread)
plt.title('Price Spread between Pepsi and Coca-Cola')
plt.show()

spread_mean = spread.mean()
spread_std = spread.std()
z_score = (spread - spread_mean) / spread_std

entry_threshold = 2.0
exit_threshold = 0.5

# Identify trade positions
positions = np.where(z_score > entry_threshold, -1, np.nan)  # Short if spread is high
positions = np.where(z_score < -entry_threshold, 1, positions)  # Long if spread is low
positions = np.where(abs(z_score) < exit_threshold, 0, positions)  # Exit

positions = pd.Series(positions, index=spread.index).ffill()

plt.figure(figsize=(12, 6))
plt.plot(positions)
plt.title('Trading Positions for Pair Trading Strategy')
plt.show()
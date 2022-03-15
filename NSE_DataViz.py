import pandas as pd
import matplotlib.pyplot as plt
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mpl_dates

plt.style.use('ggplot')

df = pd.read_csv('data.csv')
df['Date'] = pd.to_datetime(df['Date'])
ohlc = df.loc[:, ['Date','Open','High','Low','Close']]

ohlc['Date'] = ohlc['Date'].apply(mpl_dates.date2num)
fifty_df = ohlc.head(50)
fig, ax = plt.subplots()
candlestick_ohlc(ax, fifty_df.values,
                colorup='green', colordown='red')

plt.show()

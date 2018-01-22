# Candlestick
plt.figure(figsize=(8, 6))
date2num = matplotlib.dates.date2num

df_ohlc = df['Adj Close'].resample('10D').ohlc()
df_vol = df['Volume'].resample('10D').sum().to_frame()

df_ohlc.reset_index(inplace=True)
df_vol.reset_index(inplace=True)

# Converting the dates to the matplotlib's date format
df_ohlc['Date'] = df_ohlc['Date'].map(date2num)
df_vol['Date'] = df_vol['Date'].map(date2num)

# Axis 1
ax1 = plt.subplot2grid((12, 1), (0, 0), rowspan=11, colspan=1)
ax1.xaxis_date()
# Plotting the candlestick
matplotlib.finance.candlestick_ohlc(ax1, df_ohlc.values, colorup='g', width=2)
ax1.set_title('Candlestick plot', fontsize=10, color='k')
ax1.yaxis.set_label_text('Stock price ($)')

# Axis 2
ax2 = plt.subplot2grid((12, 1), (11, 0), rowspan=1, colspan=1, sharex=ax1)

# Fill between two curves
# (x, y_high, y_low)
ax2.fill_between(df_vol['Date'], df_vol['Volume'], 0, label='Volume')
ax2.xaxis.set_label_text('Date')

# General
plt.setp(ax2.xaxis.get_majorticklabels(), rotation=45)
plt.suptitle('Agilent Technologies, Inc.', fontsize=12, color='k')
plt.show()

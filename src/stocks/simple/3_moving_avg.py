# Moving average
# Preparing the data
df_ma = df.copy()
# Creating the rolling avg column
df_ma['50MA'] = df_ma['Adj Close'].rolling(window=50, min_periods=0).mean()

# Plotting
plt.figure()

# Axis 1
ax1 = plt.subplot2grid((12, 1), (0, 0), rowspan=11, colspan=1)
ax1.xaxis_date()
ax1.plot(df_ma.index, df_ma['Adj Close'], color='#56648C')
ax1.plot(df_ma.index, df_ma['50MA'], color='#FF5320', linewidth=1)
plt.title('50 days moving average', fontsize=10, color='k')
ax1.yaxis.set_label_text('Stock price ($/share)')

# Axis 2
ax2 = plt.subplot2grid((12, 1), (11, 0), rowspan=1, colspan=1, sharex=ax1)
ax2.fill_between(df_ma.index, df_ma['Volume'],
                 0, color='#56648C', label='Volume')

# Plot general
plt.setp(ax2.xaxis.get_majorticklabels(), rotation=45)
plt.suptitle('Agilent Technologies, Inc.', fontsize=12, color='k')
plt.show()

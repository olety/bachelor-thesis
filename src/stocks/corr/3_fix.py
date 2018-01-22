class StockFormatter(matplotlib.ticker.Formatter):
    def __init__(self, cols):
        self.cols = np.array(cols)

    def __call__(self, x, pos=None):
        return self.cols[np.clip(x, 0, len(self.cols) - 1).astype('int')]


# Making a correlation matrix
fig = plt.figure()

# Preparing the axis formatters
cols = list(df_corr.columns)
formatter_x = StockFormatter(cols)
formatter_y = StockFormatter(cols)

locator_x = matplotlib.ticker.MaxNLocator(10)
locator_y = matplotlib.ticker.MaxNLocator(10)

# Setting up the axis
ax = plt.subplot2grid((1, 1), (0, 0), rowspan=1, colspan=1)
ax.invert_yaxis()

# Plotting the table itself
hmap = ax.pcolormesh(df_corr.values, cmap=plt.cm.RdYlGn)
hmap.set_clim(-1, 1)  # Clipping limit
fig.colorbar(hmap)

x = ax.get_xaxis()
y = ax.get_yaxis()

# Setting tickers for X axis
x.set_major_formatter(formatter_x)
x.set_major_locator(locator_x)

plt.xticks(rotation=45)

# Setting tickers for Y axis
y.set_major_formatter(formatter_y)
y.set_major_locator(locator_y)

# Plotting the heatmap
plt.title('Stock correlation heatmap - fixed', color='k')
plt.show()

import bisect
import datetime as dt
import importlib
import logging
import os
import sys
import time

import matplotlib
from pprint import pprint
import matplotlib.pyplot as plt  # Plots q

import numpy as np  # Arrays
import pandas as pd  # DataFrames
from IPython.display import display  # IPython display
from matplotlib.finance import candlestick_ohlc  # Candlestick graph


# Pandas fancy tables
pd.set_option('display.notebook_repr_html', True)
pd.set_option('max_rows', 10)
# Matplotlib fancy plots
plt.style.use('ggplot')
# Logger setup
importlib.reload(logging)

# FORMAT = "[%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
logging.basicConfig(format='%(levelname)s | line %(lineno)s '
                    '| %(funcName)s | %(message)s',
                    level=logging.INFO, stream=sys.stdout,
                    datefmt='%H:%M:%S')
# Numpy printing setup
np.set_printoptions(threshold=10, linewidth=79, edgeitems=5)

# %% Get the data


def get_root():
    return os.path.abspath(os.sep)


STOCKS_FOLDER = os.path.join(get_root(), 'stocks')
MERGED_FOLDER = os.path.join('data', 'merged')

print('Getting data...')

# print('Single stock...')
# df = pd.read_csv(os.path.join(STOCKS_FOLDER, 'A.csv'),
#                  parse_dates=True,
#                  index_col=0)
#
# print('Merged stocks...')
# df_merged = pd.read_csv(
#     os.path.join(MERGED_FOLDER, 'stocks_merged.csv'),
#     parse_dates=True, index_col=0)

print('Merged correlation matrix...')
df_corr = pd.read_csv(os.path.join(
    MERGED_FOLDER, 'corr_matrix.csv'), index_col=0)

print('Finished getting data')

# PROBLEM - LABELS ARE WRONG
# Making a correlation matrix
fig = plt.figure()

# Setting up the axis
ax1 = plt.subplot2grid((1, 1), (0, 0), rowspan=1, colspan=1)
ax1.invert_yaxis()

hmap = ax1.pcolormesh(df_corr.values, cmap=plt.cm.RdYlGn)
hmap.set_clim(-0.5, 0.5)  # Clipping limit
fig.colorbar(hmap)

ax1.set_xticklabels(df_corr.columns)
ax1.set_yticklabels(df_corr.columns)
# Plotting the heatmap

plt.title('Stock correlation heatmap', color='k')
plt.show()


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

cdict = {
    'red': ((-0.25, 0., 0.),
            (0.24, 1., 1.),
            (0.25, 0., 0.)),

}

from matplotlib.colors import LinearSegmentedColormap
middle = LinearSegmentedColormap('Middle', cdict)

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
hmap = ax.pcolormesh(df_corr.values, cmap=middle)
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

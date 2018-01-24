# STL
from functools import partial
import os

# Data
import numpy as np
import pandas as pd
import dask.dataframe as dd
from datashader.utils import lnglat_to_meters

# Plotting
import datashader as ds
import datashader.transfer_functions as ds_tf
import bokeh.plotting as bp
from bokeh.models.tiles import WMTSTileSource
from datashader.bokeh_ext import InteractiveImage

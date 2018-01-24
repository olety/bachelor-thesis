# STL
import os
import logging
import time
# Other
import pickle
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
# Keras
import keras
from keras.callbacks import EarlyStopping
from keras.models import Sequential, load_model
from keras.layers.core import Dense, Activation, Dropout
from keras.layers.recurrent import LSTM
from keras.callbacks import EarlyStopping
from sklearn.decomposition import PCA
from sklearn.preprocessing import MinMaxScaler
# Plotting the LSTM-NN
from IPython.display import SVG
from keras.utils.vis_utils import model_to_dot
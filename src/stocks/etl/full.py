# %% Imports
import datetime as dt
import gc
import importlib
import logging
import os
import re
import sys
import time

import bs4 as bs  # BeautifulSoup, HTML scraping
import matplotlib.pyplot as plt  # Plots q
import numpy as np  # Arrays
import pandas as pd  # DataFrames
import pandas_datareader as web  # Gets stock data from Yahoo
import requests  # HTTP requests
from tqdm import tqdm  # Progress bar

# Describe these options
# Pandas fancy tables
pd.set_option('display.notebook_repr_html', True)
pd.set_option('max_rows', 100)
# Matplotlib fancy plots
plt.style.use('ggplot')
# Logger setup
importlib.reload(logging)

LOGGING_FORMAT = '%(levelname)s | line %(lineno)s | %(funcName)s | %(message)s'
logging.basicConfig(format=LOGGING_FORMAT, level=logging.INFO,
                    stream=sys.stdout, datefmt='%H:%M:%S')

# Numpy printing setup
np.set_printoptions(threshold=100, linewidth=79, edgeitems=5)


def get_root():
    return os.path.abspath(os.sep)


def get_snp_tickers():
    '''
    Gets the list of S&P500 stocks from wikipedia

    Throws an exception if it can't get the data
    '''

    # We'll be using wikipedia as a main data source
    URL = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
    logging.debug('Getting the wikipedia article...')
    resp = requests.get(URL)

    # If we can't get the page, just throw an exception
    logging.debug('Checking the response code...')
    if resp.status_code != 200:
        raise Exception('Couldn\'t access the url.'
                        'fResponse code {resp.status_code}')
    # We've gotten the page by now; start parsing the response
    soup = bs.BeautifulSoup(resp.text, 'html5lib')
    # Find the table containing the tickers
    logging.debug('Finding the table containing the tickers...')
    for table in soup.findAll('table', {'class': 'wikitable sortable'}):
        try:
            # We're searching for a table that has a 'Ticker symbol' as its
            # first column name
            if table.findAll('th')[0].a.contents[0] == 'Ticker symbol':
                res_table = table
        except Exception:
            pass
    # Start extracting the tickers from the table
    logging.debug('Extracting the tickers...')
    res_arr = []
    for row in res_table.findAll('tr')[1:]:
        # Replacing dots with dashes because otherwise we won't be able to
        # download them from yahoo finance - cleaning the data
        res_arr.append(
            row.findAll('td')[0]
            .a.contents[0]
            .replace(',', '-').replace('.', '-')
        )
    return res_arr


def save_tickers(folder='data/tickers', fname='tickers.csv'):
    '''
    Saves tickers got by get_snp_tickers into a file using Pickle.

    Throws an exception if something goes wrong.
    '''
    logging.debug('Getting the tickers...')
    tickers = pd.DataFrame(get_snp_tickers())
    if tickers.shape[0] != 505:
        raise Exception('Bad ticker count - '
                        '{} instead of 505'.format(len(tickers)))
    logging.debug('Gotten tickers')
    tickers.columns = ['Ticker']
    display(tickers)
    # Sorting the tickers alphabetically
    logging.debug('Sorting the tickers...')
    tickers.sort_values(by='Ticker', inplace=True)
    logging.debug('Tickers after sorting')
    display(tickers)
    # Saving the tickers
    fpath = os.path.join(os.getcwd(), folder, fname)
    logging.debug('Creating the destination folder...')
    if not os.path.exists(os.path.dirname(fpath)):
        os.makedirs(os.path.dirname(fpath))
    logging.debug(f'Saving the tickers to {fpath}')

    tickers.to_csv(fpath, index=False)
    logging.info(f'Saved the tickers to {fpath}')

    return tickers


def get_stock_data(start_dt, end_dt, reload_tickers=False,
                   max_tries=50, timeout=2, provider='yahoo',
                   ticker_folder=os.path.join('data', 'tickers'),
                   ticker_fname='tickers.csv',
                   dest_folder=os.path.join('data', 'stocks')):
    '''
    Gets stock data of S&P500 from yahoo and saves it in the {folder}/{tick}.csv

    Throws an exception is anything goes wrong.
    '''
    logging.debug('Obtaining the tickers...')
    if reload_tickers:
        tickers = save_tickers()
    else:
        tickers = pd.read_csv(os.path.join(os.getcwd(),
                                           ticker_folder, ticker_fname))
    logging.debug('Obtained the tickers...')
    logging.debug(tickers)
    # We have to check whether the dest folder exists
    dest_path = os.path.join(os.getcwd(), dest_folder)
    if not os.path.exists(dest_path):
        logging.debug('Creating the destination folder')
        os.makedirs(dest_path)

    # Downloading the prices
    logging.debug('Starting processing tickers...')
    down_cnt, to_down_cnt = 0, len(tickers)
    for index, ticker in tqdm(tickers.itertuples(), desc='Tickers processed',
                              leave=False, file=sys.stderr, unit='company',
                              total=tickers.shape[0]):
        df = None
        logging.debug(f'Starting a new outer loop iteration for {ticker}')
        dest_fpath = os.path.join(dest_path, f'{ticker}.csv')
        if not os.path.exists(dest_fpath):
            # Try to download the stock for max_tries tries, waiting
            # for timeout in between tries
            pbar = tqdm(range(max_tries), desc='Number of tries',
                        leave=False, file=sys.stderr, unit='try')
            tries = max_tries
            while tries > 0:
                pbar.update(1)
                try:
                    logging.debug(f'Trying to get {ticker} data'
                                  f' from {provider}...')
                    df = web.DataReader(ticker, provider, start_dt, end_dt)
                    tries = 0
                    down_cnt += 1
                except Exception as e:
                    tries -= 1
                    logging.debug(e)
                    logging.debug(f'{provider} has denied our request - '
                                  f'sleeping for {timeout} seconds')
                    time.sleep(timeout)
            pbar.close()

            if df is None:
                logging.debug(f'Couldn\'t get the {ticker} data. Continuing')
                continue

            logging.debug(f'Successfully got {ticker} data from {provider}. '
                          'Now saving it...')
            df.to_csv(dest_fpath)
            logging.debug(f'Saved the {ticker} data.')
        else:
            to_down_cnt -= 1
            logging.debug(f'Not downloading data for {ticker}, '
                          'since we already have it')
    logging.info('Finished processing all tickers!')
    logging.info(f'Downloaded: {down_cnt}/{to_down_cnt} items')
    logging.info(f'You can find the results in the folder {dest_path}')


def conv_nyse_tickers(dest_fpath=os.path.join('data', 'tickers', 'NYSE_proc.csv'),
                      source_fpath=os.path.join('data', 'tickers', 'NYSE.csv')):
    # Reading the file
    logging.info('Reading the NYSE tickers file')
    s = pd.read_csv(source_fpath)['Symbol']
    s.str.strip()
    # Started cleaning - getting the rows that contain '^'
    logging.debug('Processing hat rows...')
    contains_hat = s.str.contains('\^')
    # Cleaning - selecting the rows that contain a hat
    s_hat = s[contains_hat]
    # Cleaning - changing hat to -P and dots in those rows to ''
    s_hat = s_hat.str.replace('^', '-P')
    s_hat = s_hat.str.replace('.', '')
    # Cleaning - in other rows, replace dows with dashes
    logging.debug('Processing no-hat rows...')
    s = s[contains_hat == False]
    s = s.str.replace('.', '-')
    # Merge two series and sort them
    logging.debug('Merging series together...')
    s.append(s_hat)
    s.sort_values(inplace=True)
    # Save the output to the file
    logging.info('Finished processing the NYSE tickers file.')
    logging.info(f'You can find your results in {dest_fpath}')
    df = s.to_frame()
    df.columns = ['Ticker']
    df.to_csv(dest_fpath, index=False)

# %% Data transformation
# In this step, we want to get the combined DataFrame
# of all adjusted closing prices


def list_csv(path):
    for f in os.listdir(path):
        if f.endswith('.csv'):
            yield f


def save_timearr(stock_dir, save_dir='data', save_fname='time_index.csv',
                 example_timefile='GHC.csv'):
    time_df = pd.read_csv(os.path.join(
        stock_dir, example_timefile), index_col=0)
    time_arr = time_df.index.values
    np.savetxt(os.path.join(save_dir, save_fname),
               time_arr, delimiter=',', fmt="%s")


def get_timearr_file(fdir='data', fname='time_index.csv'):
    fpath = os.path.join(fdir, fname)
    if not os.path.isfile(fpath):
        raise Exception('Couldn\'t find the time_index.csv, please '
                        'invoke save_timearr before get_timearr')
    return np.loadtxt(fpath, delimiter=',', dtype=np.datetime64)


def get_timearr(stock_dir, example_timefile='GHC.csv'):
    time_df = pd.read_csv(os.path.join(
        stock_dir, example_timefile), index_col=0)
    return time_df.index.values


def process_nyse(stock_dir, save_dir, time_arr, reload_data=False):
    if not os.path.isdir(save_dir):
        os.makedirs(save_dir)

    for stock_fname in tqdm(list_csv(stock_dir)):
        if not reload_data and os.path.isfile(os.path.join(save_dir,
                                                           stock_fname)):
            continue
        stock = pd.read_csv(os.path.join(stock_dir, stock_fname), index_col=0)
        stock = stock.reindex(time_arr, fill_value=np.nan)
        stock.to_csv(os.path.join(save_dir, stock_fname))
    gc.collect()


def get_per_diff(old, new):
    return abs(new - old) / old

# Scales between - and 1


def scale_series(col):
    return (col - col.min()) / (col.max() - col.min())


def merge_dfs(stock_folder, save_folder, save_fname='stocks_all_merged.csv',
              reload_data=False, add_per_oc=True, add_per_lohi=True,
              add_volume=True, scale_features=False):
    '''
    Merges the stock csv files into one big file with all adj. closes

    Raises an exception if something goes wrong.
    '''
    if (os.path.isfile(os.path.join(save_folder, save_fname)) and
            not reload_data):
        logging.warning('The target file is already present in the save_folder.'
                        ' Please use the reload_data argument to overwrite it.')
        return
    logging.debug('Started merging the stock data - getting the files')
    fnames = sorted(list(list_csv(stock_folder)))
    logging.debug('Number of csv files in the folder: {}'.format(len(fnames)))
    logging.debug(f'Filelist: {fnames}')

    time_arr = get_timearr(stock_folder, fnames[0])
    to_stack = []
    col_names = []

    logging.debug('Starting merging dataframes')
    for cur_fname in tqdm(fnames, desc='Files processed', file=sys.stdout,
                          leave=True, unit='file'):
        cur_fpath = os.path.join(stock_folder, cur_fname)
        cur_ticker = cur_fname[:-4]
        col_names.append(cur_ticker)

        logging.debug(f'Processing the file {cur_fname}')

        cur_df = pd.read_csv(cur_fpath, index_col=0)

        if scale_features:
            cur_df['Adj Close'] = scale_series(cur_df['Adj Close'])
            cur_df['Volume'] = scale_series(cur_df['Volume'])

        if add_volume:
            col_names.append(f'{cur_ticker}_Vol')
        else:
            cur_df.drop(['Volume'], inplace=True, axis=1)

        if add_per_oc:
            cur_df['PerOC'] = get_per_diff(cur_df['Open'], cur_df['Close'])
            col_names.append(f'{cur_ticker}_OC')

        if add_per_lohi:
            cur_df['PerLH'] = get_per_diff(cur_df['Low'], cur_df['High'])
            col_names.append(f'{cur_ticker}_LH')

        cur_df.drop(['Open', 'Close', 'High', 'Low'],
                    inplace=True, axis=1)

        to_stack.append(cur_df.as_matrix())

    # It's faster to just stack a list of numpy arrays than to try and merge dfs
    merged_df = pd.DataFrame(np.concatenate(to_stack, axis=1),
                             index=time_arr, columns=col_names)
    logging.debug('Finished merging dataframes')
    save_path = os.path.join(save_folder, save_fname)

    logging.debug(f'Saving the data to {save_path}')
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    merged_df.to_csv(save_path)
    return merged_df


def make_corr_matrix(merge_folder, save_folder,
                     merged_close_fname='stocks_close_merged.csv',
                     save_fname='corr_matrix.csv', reload_data=False):
    if (os.path.isfile(os.path.join(save_folder, save_fname)) and
            not reload_data):
        logging.warning('The target file is already present in the save_folder.'
                        ' Please use the reload_data argument to overwrite it.')
        return
    merged_path = os.path.join(merge_folder, merged_close_fname)
    save_path = os.path.join(save_folder, save_fname)
    logging.debug(f'Opening the merged closes folder at {merged_path}')
    merged_df = pd.read_csv(merged_path)
    corr_df = merged_df.corr()
    logging.debug(f'Saving the corr_df to {save_path}')
    corr_df.to_csv(save_path)
    return corr_df


# %% Function execution
# Constants
# We want to get the data from 2000 till 2017
START_DT = dt.datetime(2000, 1, 1)
END_DT = dt.datetime(2017, 1, 1)
# We want to place the merged file in data/merged
STOCK_FOLDER = os.path.join('stocks')  # get_root(),
MERGED_FOLDER = os.path.join('data', 'merged')
# save_tickers()
# conv_nyse_tickers()
# get_stock_data(START_DT, END_DT, max_tries=1,
#                ticker_fname='NYSE_proc.csv',
#                dest_folder=os.path.join('data', 'nyse'), timeout=0.1,
#                provider='yahoo')
merge_dfs(STOCK_FOLDER, MERGED_FOLDER, reload_data=True)
merge_dfs(STOCK_FOLDER, MERGED_FOLDER, save_fname='stocks_all_scaled.csv',
          reload_data=True, scale_features=True)
merge_dfs(STOCK_FOLDER, MERGED_FOLDER, save_fname='stocks_close_merged.csv',
          reload_data=True, add_per_oc=False, add_per_lohi=False, add_volume=False)
make_corr_matrix(MERGED_FOLDER, MERGED_FOLDER, reload_data=True)

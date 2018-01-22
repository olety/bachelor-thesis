

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
        tickers = pd.read_csv(os.path.join(ticker_folder, ticker_fname))
    logging.debug('Obtained the tickers...')
    logging.debug(tickers)
    # We have to check whether the dest folder exists
    dest_path = dest_folder
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

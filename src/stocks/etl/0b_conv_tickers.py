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
    # Cleaning - in other rows, replace dots with dashes
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

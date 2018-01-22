def get_per_diff(old, new):
    return abs(new - old) / old


def merge_dfs(stock_folder, save_folder, save_fname='stocks_all_merged.csv',
              reload_data=False, add_per_oc=True, add_per_lohi=True,
              add_volume=True):
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

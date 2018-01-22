# We want to get the data from 2000 till 2017
START_DT = dt.datetime(2000, 1, 1)
END_DT = dt.datetime(2017, 1, 1)
# We want to place the merged file in data/merged
STOCK_FOLDER = os.path.join('data', 'stocks')
MERGED_FOLDER = os.path.join('data', 'merged')

# Downloading the data
get_stock_data(START_DT, END_DT, max_tries=5, ticker_fname='NYSE.csv',
               dest_folder=STOCK_FOLDER, timeout=0.1, provider='yahoo')

# Reindexing the csvs so we can np.concatenate them later
reindex_csv(STOCK_FOLDER, STOCK_FOLDER, get_timearr(STOCK_FOLDER, 'A.csv'),
            reload_data=True)

# Merging the dataframes
merge_dfs(STOCK_FOLDER, MERGED_FOLDER, reload_data=True)

merge_dfs(STOCK_FOLDER, MERGED_FOLDER, save_fname='stocks_close_merged.csv',
          reload_data=True, add_per_oc=False, add_per_lohi=False, add_volume=False)

# Making the correlation matrix
make_corr_matrix(MERGED_FOLDER, MERGED_FOLDER, reload_data=True)

MERGED_FOLDER = os.path.join('data', 'merged')

MERGED_FNAME = 'stocks_all_merged.csv'
MERGED_PATH = os.path.join(MERGED_FOLDER, MERGED_FNAME)

# # We need to use index_col=0 to set it as a main
logging.info('Reading the merged dataset...')
df_merged = pd.read_csv(MERGED_PATH, index_col=0)
df_merged.fillna(0, inplace=True)
df_merged.reset_index(drop=True, inplace=True)
logging.info('Finished processing the merged dataset')

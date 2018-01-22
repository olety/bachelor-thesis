plt.style.use('seaborn')  # Fancier matplotlib plots

STOCKS_FOLDER = os.path.join('data', 'stocks')
MERGED_FOLDER = os.path.join('data', 'merged')

print('Getting data...')

print('Single stock...')
df = pd.read_csv(os.path.join(STOCKS_FOLDER, 'A.csv'),
                 parse_dates=True,
                 index_col=0)

print('Merged stocks...')
df_merged = pd.read_csv(
    os.path.join(MERGED_FOLDER, 'stocks_close_merged.csv'),
    parse_dates=True, index_col=0)

print('Finished getting data')

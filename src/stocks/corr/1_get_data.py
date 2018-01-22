def get_root():
    return os.path.abspath(os.sep)


STOCKS_FOLDER = os.path.join(get_root(), 'stocks')
MERGED_FOLDER = os.path.join('data', 'merged')

print('Getting data - merged correlation matrix...')

df_corr = pd.read_csv(
    os.path.join(MERGED_FOLDER, 'corr_matrix.csv'), index_col=0)
print('Finished getting data')

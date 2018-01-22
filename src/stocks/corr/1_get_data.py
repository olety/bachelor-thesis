plt.style.use('ggplot')
MERGED_FOLDER = os.path.join('data', 'merged')

print('Getting data...')

print('Merged correlation matrix...')
df_corr = pd.read_csv(os.path.join(
    MERGED_FOLDER, 'corr_matrix.csv'), index_col=0)

print('Finished getting data')

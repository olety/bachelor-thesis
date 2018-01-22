plt.style.use('seaborn')  # Fancier matplotlib plots

STOCKS_FOLDER = os.path.join('data', 'stocks')

print('Getting data...')

print('Single stock...')
df = pd.read_csv(os.path.join(STOCKS_FOLDER, 'A.csv'),
                 parse_dates=True,
                 index_col=0)

print('Finished getting data')

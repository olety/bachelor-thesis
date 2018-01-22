FILE_PATH = os.path.join('data', 'youtube-u-growth', 'out')

# Pandas
df = pd.read_csv(FILE_PATH, skiprows=2, sep=' ',
                 names=['source', 'target', 'weight', 'date'])
df['date'] = pd.to_datetime(df['date'], unit='s')  # Converting date to datetime
df.describe(include='all')  # Checking the df. The weight is always 1
df.drop('weight', axis=1, inplace=True)  # Dropping weight because it's const

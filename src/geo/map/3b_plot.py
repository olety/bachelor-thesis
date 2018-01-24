def plot(year, title, legend_title, ind='IT.CEL.SETS.P2', show_values_inside=False):
    # Customizing the data connection to be able to retrieve different indicators
    con = sqlite3.connect(os.path.join(get_root(), 'wdi', 'database.sqlite'))

    df = pd.read_sql_query(
        'SELECT * FROM Country c '
        'INNER JOIN Indicators i ON c.CountryCode = i.CountryCode '
        f'WHERE i.IndicatorCode="{ind}"', con)

    df = df.T.drop_duplicates().T  # Removing duplicate columns
    df = df.infer_objects()  # Correct object types

    df_plot = df[(df['Year'] == year) & (df['Region'] != '')]
    df_plot = df_plot.iloc[:, [0, 1, -1]]

    if (df_plot['Value'].max() <= 0):
        raise Exception('No data to plot')

    # Normalizing the data to show percentages
    norm_min = df_plot['Value'].min()
    norm_max = df_plot['Value'].max()
    df_plot['Value'] = (df_plot['Value'] - norm_min) / (norm_max - norm_min)

    # Using countrycode as an index to use it in draw_plot
    df_plot.set_index('CountryCode', inplace=True)
    df_plot.dropna(inplace=True)

    # Calculating the bin distribution
    _, bins = np.histogram(df_plot['Value'], bins=5)
    df_plot['bin'] = np.digitize(df_plot['Value'], bins)
    bins_real = norm_min + bins * (norm_max - norm_min)

    return df, draw_plot(df_plot, bins, bins_real, year, title, legend_title, show_values_inside)

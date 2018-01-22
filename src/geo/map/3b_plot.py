# Getting the data for a particular year
df_plot = df[(df['Year'] == year) & (df['Region'] != '')]
df_plot = df_plot.iloc[:, [0, 1, -1]]

if (df_plot['Value'].max() <= 0):
    raise Exception('No data to plot')

# Normalizing the data to show percentages
norm_min = df_plot['Value'].min()
norm_max = df_plot['Value'].max()

df_plot['Value'] = (df_plot['Value'] - norm_min) / (norm_max - norm_min)

# Using country code as an index for further use in draw_plot
df_plot.set_index('CountryCode', inplace=True)
df_plot.dropna(inplace=True)

# Determining the color bins
_, bins = np.histogram(df_plot['Value'], bins=5)
df_plot['bin'] = np.digitize(df_plot['Value'], bins)
bins_real = norm_min + bins * (norm_max - norm_min)

# Calling the plot function
fig, ax = draw_plot(df_plot, bins, bins_real, year, title, legend_title)
plt.show()

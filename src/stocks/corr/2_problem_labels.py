# PROBLEM - LABELS ARE WRONG
# Making a correlation matrix
fig = plt.figure()

# Setting up the axis
ax1 = plt.subplot2grid((1, 1), (0, 0), rowspan=1, colspan=1)
ax1.invert_yaxis()

hmap = ax1.pcolormesh(df_corr.values, cmap=plt.cm.RdYlGn)
hmap.set_clim(-0.5, 0.5)  # Clipping limit
fig.colorbar(hmap)

ax1.set_xticklabels(df_corr.columns)
ax1.set_yticklabels(df_corr.columns)

# Plotting the heatmap
plt.title('Stock correlation heatmap', color='k')
plt.show()

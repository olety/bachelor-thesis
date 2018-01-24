def draw_plot(df_plot, bins, bins_real, year, title, legend_title):
    # Preparation
    cm = plt.get_cmap('Greens')
    scheme = [cm(i / len(bins)) for i in range(len(bins))]
    cmap = matplotlib.colors.ListedColormap(scheme)
    shapefile = 'shape/ne_10m_admin_0_countries'

    # Creating figure and axis. We need 1 axis for the plot and 1 for legend
    fig = plt.figure(figsize=(18, 18))
    ax = plt.subplot2grid((2, 2), (0, 0), rowspan=2, colspan=2)

    # Creating a map and reading it from a shape file
    m = Basemap(lon_0=0, projection='robin', resolution='c')
    m.readshapefile(shapefile, 'units', color='#444444', linewidth=.2)

    # Drawing the country and continent borders
    m.drawcoastlines()
    m.drawcountries()

    # Iterating through the map units because it has the country info
    # df_plot contains kpis and we are using a country as a key
    for info, shape in zip(m.units_info, m.units):
        iso3 = info['ADM0_A3']
        if iso3 in df_plot.index:
            color = scheme[df_plot.loc[iso3]['bin'] - 1]
        else:
            color = '#dddddd'
        # Adding a polygon for each country
        ax.add_patch(Polygon(np.array(shape), facecolor=color))

    # Creating a legend
    ax_legend = fig.add_axes([0.35, 0.25, 0.3, 0.03], zorder=3)
    cb = matplotlib.colorbar.ColorbarBase(
        ax_legend, ticks=bins, boundaries=bins, cmap=cmap, orientation='horizontal')
    ax_legend.set_xticklabels([f'{i:.0%}' for i in bins])

    # Ticks inside legend's color boxes
    if show_values_inside:
        for i in range(len(bins_real) - 1):
            text = f'{bins_real[i]:.1f}-{bins_real[i+1]:.1f}'
            x_indent = cb._ticker()[0][i] + 0.09 - len(text) / 165
            ax_legend.annotate(text, xy=(x_indent, 0.4))

    # Title and legend title
    ax.set_title(title, fontsize=17)
    ax_legend.set_title(legend_title)

    return fig, ax

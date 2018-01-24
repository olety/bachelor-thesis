# Create a bokeh plot
p = base_plot()
# Use the map as the background
tile_renderer = p.add_tile(WMTSTileSource(url=geourl))
tile_renderer.alpha = 0.7
# Plot the datashader image on top of the bokeh one
InteractiveImage(p, image_callback)  # Dropoffs
InteractiveImage(p, partial(image_callback, which='pickup'))  # Pickups

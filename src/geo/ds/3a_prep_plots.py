geourl = 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{Z}/{Y}/{X}.jpg'
sw = lnglat_to_meters(-87.92, 41.67)  # lon = x, lat = y
ne = lnglat_to_meters(-87.53, 42.03)
x_range, y_range = zip(sw, ne)

def base_plot(width=1000, height=1000):
    p = bp.figure(plot_width=width, plot_height=height,
                  x_range=x_range, y_range=y_range, outline_line_color=None,
                  min_border=0, min_border_left=0, min_border_right=0,
                  min_border_top=0, min_border_bottom=0)
    # Making everything invisible to just show the map
    p.axis.visible = False
    p.xgrid.grid_line_color = None
    p.ygrid.grid_line_color = None

    return p


def image_callback(x_range, y_range, width, height, cmap=ds.colors.Hot, which='dropoff'):
    # Create a canvas
    cvs = ds.Canvas(width, height, x_range, y_range)
    # Aggreagate points
    count = cvs.points(df_comp, f'{which}_x', f'{which}_y')
    # Draw points
    image = ds_tf.shade(count, cmap=cmap)
    # Dynspread dynamically adjusts the pixel size
    return ds_tf.dynspread(image, threshold=0.75, max_px=8)

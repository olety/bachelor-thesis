def plot_edges(edges, name=None, plot_height=500, plot_width=500):
    canvas = ds.Canvas(plot_height=plot_height, plot_width=plot_width)
    return ds_tf.shade(canvas.line(edges, 'x', 'y', agg=ds.count()), name=name)


def plot_vertices(verts, name=None, cat=None, plot_height=500, plot_width=500, spread=0):
    canvas = ds.Canvas(plot_height=plot_height, plot_width=plot_width)
    aggregator = None if cat is None else ds.count_cat(cat)
    agg = canvas.points(verts, 'x', 'y', aggregator)
    # Vertices will be plotted in red
    return ds_tf.spread(ds_tf.shade(agg, name=name, cmap=['#ff0000']), px=spread)


def plot_full(verts, edges, name='', cat=None,
              plot_height=500, plot_width=500, spread=0):
    # Determining plot
    xr = verts.x.min(), verts.x.max()
    yr = verts.y.min(), verts.y.max()
    canvas = ds.Canvas(plot_height=plot_height,
                       plot_width=plot_width, x_range=xr, y_range=yr)
    # Aggregating by gategory is possible
    aggregator = None if cat is None else ds.count_cat(cat)
    agg = canvas.points(verts, 'x', 'y', aggregator)
    # Plotting vertices
    np = ds_tf.spread(ds_tf.shade(agg, name=name + ' verts',
                                  cmap=['#ff0000']), px=spread)
    # Protting edges
    ep = ds_tf.shade(canvas.line(
        edges, 'x', 'y', agg=ds.count()), name=name + ' edges')

    return ds_tf.stack(ep, np, how="over", name=name)

# Setting up the plot
hdg_style = {}  # Creating a style dictionary
hdg_style['layout'] = \
    hdg_subgraph.layout_fruchterman_reingold(maxiter=1000, area=hdg_vcount**3)
hdg_style['vertex_size'] = 0.001
hdg_style['bbox'] = (1024, 1024)
hdg_style['vertex_shape'] = 'circle'
hdg_style['edge_width'] = 0.1
hdg_style['target'] = 'plot_naive.svg'

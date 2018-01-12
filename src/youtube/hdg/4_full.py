# Selecting high degree nodes
hdg_vertices = g.vs.select(_degree_ge=800)  # Select vertices with a high degree
hdg_subgraph = hdg_vertices.subgraph()  # Create a new subgraph
hdg_vcount = hdg_subgraph.vcount()  # Will be used later in the layout calculation
# Check the number of vertices
print(f'Number of vertices in the subgraph: {hdg_vcount}')

# Setting up the plot
hdg_style = {}  # Creating a style dictionary
hdg_style['layout'] = \
    hdg_subgraph.layout_fruchterman_reingold(maxiter=1000, area=hdg_vcount**3)
hdg_style['vertex_size'] = 0.001
hdg_style['bbox'] = (500, 500)
hdg_style['vertex_shape'] = 'circle'
hdg_style['edge_width'] = 0.1

# Plotting
save_fname = 'plot_naive.svg'
ig.plot(hdg_subgraph, save_fname, **hdg_style)

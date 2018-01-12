# Clustering the high degree subgraph
hdg_imap = hdg_subgraph.community_infomap()
hdg_membership = hdg_imap.membership

# Selecting random colors for groups using a list comprehension with an f-string
community_colors = [f'#{random.randint(0, 0xFFFFFF):06x}' for comm in hdg_imap]
# Creating a list that will be used to assign color to every vertice
vert_colors = list(range(hdg_subgraph.vcount()))

# Initializing lists that will hold the edge attributes
edge_colors = []
edge_weights = []

# Assigning the vertice color based on their community
for comm_id, comm in enumerate(hdg_imap):
    for vert in comm:
        vert_colors[vert] = community_colors[comm_id]

# Assigning the edge color and weight based on the vertices it connects
# Adding weights will make the group separation more visible
for edge in hdg_subgraph.es:
    if hdg_membership[edge.source] == hdg_membership[edge.target]:
        edge_colors.append(vert_colors[edge.source])
        edge_weights.append(3 * hdg_vcount)
    else:
        edge_colors.append('#dbdbdb')
        edge_weights.append(0.1)

# Styling the plot - graph properties
hdg_subgraph.vs['color'] = vert_colors  # Adding color as a vertice property
hdg_subgraph.es['color'] = edge_colors  # Adding color as an edge property
hdg_subgraph.es['weight'] = edge_weights  # Adding weight as an edge property

# Styling the plot - style dictionary
hdg_comm_style = {}
hdg_comm_style['layout'] = \
    hdg_subgraph.layout_fruchterman_reingold(maxiter=1000,
                                             weights=hdg_subgraph.es['weight'],
                                             area=hdg_vcount**3,
                                             repulserad=hdg_vcount**3)
hdg_comm_style['bbox'] = (500, 500)
hdg_comm_style['vertex_size'] = 0.5
hdg_comm_style['vertex_shape'] = 'circle'
hdg_comm_style['edge_width'] = 0.1
hdg_comm_style['palette'] = ig.PrecalculatedPalette(community_colors)

# Plotting
save_fname = 'plot_infomap.svg'
ig.plot(hdg_imap, save_fname, **hdg_comm_style)

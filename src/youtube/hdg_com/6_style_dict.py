# Styling the plot - style dictionary
hdg_comm_style = {}
hdg_comm_style['layout'] = \
    hdg_subgraph.layout_fruchterman_reingold(maxiter=1000,
                                             weights=hdg_subgraph.es['weight'],
                                             area=hdg_vcount**3,
                                             repulserad=hdg_vcount**3)
hdg_comm_style['bbox'] = (1024, 1024)
hdg_comm_style['vertex_size'] = 0.5
hdg_comm_style['vertex_shape'] = 'circle'
hdg_comm_style['edge_width'] = 0.1
hdg_comm_style['target'] = 'plot_infomap.svg'
hdg_comm_style['palette'] = ig.PrecalculatedPalette(community_colors)
hdg_comm_style['edge_order_by'] = 'weight'
# hdg_comm_style['mark_groups'] = True # Uncomment if you want to delineate the groups

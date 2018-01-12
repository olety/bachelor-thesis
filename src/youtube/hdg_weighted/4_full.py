hdg_pgrank = hdg_subgraph.pagerank()
hdg_pgrank_arr = np.array(hdg_pgrank)

# Style dict
hdg_comm_style = {}
hdg_comm_style['layout'] = \
    hdg_subgraph.layout_fruchterman_reingold(maxiter=1000,
                                             weights=hdg_subgraph.es['weight'],
                                             area=hdg_vcount**3,
                                             repulserad=hdg_vcount**3)
hdg_comm_style['bbox'] = (500, 500)
hdg_comm_style['vertex_size'] = hdg_pgrank_arr * 3000
hdg_comm_style['vertex_shape'] = 'circle'
hdg_comm_style['edge_width'] = 0.1
hdg_comm_style['palette'] = ig.PrecalculatedPalette(community_colors)

save_fname = 'plot_pagerank_fg.svg'
ig.plot(hdg_imap, save_fname, **hdg_comm_style)

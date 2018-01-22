# Creating vertex/edge dataframes
g_df_vert = pd.DataFrame(g.vs.indices, columns=['name'])
g_df_edge = pd.DataFrame(edge_matrix, columns=['source', 'target'])

# Trying to plot the entire graph. Using the random layout because the fg one crashed the server
g_layout_fg = ds.layout.random_layout(g_df_vert, g_df_edge, seed=55)
g_bundling_fg = ds_b.directly_connect_edges(g_layout_fg, g_df_edge)

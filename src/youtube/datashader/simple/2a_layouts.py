# Creating the vertice/edge dfs
lv_df_vert = pd.DataFrame(louvain_graph.vs.indices, columns=['name'])
lv_df_edge = pd.DataFrame([(e.source, e.target)
                           for e in louvain_graph.es], columns=['source', 'target'])

# Force directed layout
lv_layout_f = ds.layout.forceatlas2_layout(lv_df_vert, lv_df_edge)
lv_bundling_f = ds_b.hammer_bundle(lv_layout_f, lv_df_edge)
lv_bundling_dc_f = ds_b.directly_connect_edges(lv_layout_f, lv_df_edge)

# Random layout
lv_layout_r = ds.layout.random_layout(lv_df_vert, lv_df_edge)
lv_bundling_r = ds_b.hammer_bundle(lv_layout_r, lv_df_edge)
lv_bundling_dc_r = ds_b.directly_connect_edges(lv_layout_dc_r, lv_df_edge)

# Circlular layout
lv_layout_c = ds.layout.circular_layout(lv_df_vert, lv_df_edge)
lv_bundling_c = ds_b.hammer_bundle(lv_layout_c, lv_df_edge)
lv_bundling_dc_c = ds_b.directly_connect_edges(lv_layout_c, lv_df_edge)

# Preparing the layouts
lv_layout_comm = ds.layout.forceatlas2_layout(
    lv_df_comm, lv_df_edge, linlog=True)
lv_bundling_comm = ds_b.hammer_bundle(lv_layout_comm, lv_df_edge)

# Spread
ds_tf.Image(plot_full(lv_layout_comm, lv_bundling_comm, 'Full - Force-directed - Categorized',
                      cat='cat', spread=1, plot_height=1000, plot_width=1000))

# No spread
ds_tf.Image(plot_full(lv_layout_comm, lv_bundling_comm, 'Full - Force-directed - Categorized',
                      cat='cat', spread=1, plot_height=1000, plot_width=1000))

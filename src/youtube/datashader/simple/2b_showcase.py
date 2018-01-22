# Making the plots
lv_plots = [
    # Force-directed layout
    # Directly connected
    plot_vertices(
        lv_layout_f, 'Vertices - Force-directed - Directly connected'),
    plot_edges(lv_bundling_dc_f, 'Edges - Force-directed - Directly connected'),
    plot_full(lv_layout_f, lv_bundling_dc_f,
              'Full - Force-directed - Directly connected'),
    # Bundled
    plot_vertices(lv_layout_f, 'Vertices - Force-directed - Bundled'),
    plot_edges(lv_bundling_f, 'Edges - Force-directed - Bundled'),
    plot_full(lv_layout_f, lv_bundling_f, 'Full - Force-directed - Bundled'),
    # Random layout
    # Directly connected
    plot_vertices(lv_layout_r, 'Vertices - Random - Directly connected'),
    plot_edges(lv_bundling_dc_r, 'Edges - Random - Directly connected'),
    plot_full(lv_layout_r, lv_bundling_dc_r,
              'Full - Random - Directly connected'),
    # Bundled
    plot_vertices(lv_layout_r, 'Vertices - Random - Bundled'),
    plot_edges(lv_bundling_r, 'Edges - Random - Bundled'),
    plot_full(lv_layout_r, lv_bundling_r, 'Full - Random - Bundled'),
    # Circular layout
    # Directly connected
    plot_vertices(lv_layout_c, 'Vertices - Circular - Directly connected'),
    plot_edges(lv_bundling_dc_c, 'Edges - Circular - Directly connected'),
    plot_full(lv_layout_c, lv_bundling_dc_c,
              'Full - Circular - Directly connected'),
    # Bundled
    plot_vertices(lv_layout_c, 'Vertices - Circular - Bundled'),
    plot_edges(lv_bundling_c, 'Edges - Circular - Bundled'),
    plot_full(lv_layout_c, lv_bundling_c, 'Full - Circular - Bundled')
]

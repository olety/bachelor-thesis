# Selecting high degree nodes
hdg_vertices = g.vs.select(_degree_ge=800)  # Select vertices with a high degree
hdg_subgraph = hdg_vertices.subgraph()  # Create a new subgraph
hdg_vcount = hdg_subgraph.vcount()  # Will be used later in the layout calculation
# Check the number of vertices
print(f'Number of vertices in the subgraph: {hdg_vcount}')

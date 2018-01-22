# Converting dataframe to the igraph's graph - Preparations
# Creating a blank graph
g = ig.Graph()

# Creating arrays for edges, vertices and edge attributes
edge_df = df.loc[:, 'source':'target']
edge_matrix = edge_df.as_matrix()
vertices_unique = pd.unique(edge_matrix.ravel('K'))

# The ids are starting from zero
vertice_array = np.arange(0, vertices_unique.shape[0])
print('Created a blank graph and element arrays')

# Adding vertices
g.add_vertices(vertice_array.tolist())
print('Added vertices')

# Changing the edges from names to ids
vertice_ids = dict(zip(vertices_unique, vertice_array))
rename_edges = np.vectorize(lambda x: vertice_ids[x])
edge_matrix = rename_edges(edge_matrix)
print('Renamed edges in the edge_matrix to their ids')

# Adding edges
g.add_edges(edge_matrix)
print('Added edges')

# Adding edge attributes
g.es['date'] = df['date'].as_matrix()
print('Added edge attributes')
print('Displaying summary')
ig.summary(g)

def test_edge_renaming():
    # Convert the source dataframe to a numpy
    orig_edge_matrix = df.loc[:, 'source':'target'].as_matrix()
    for orig_edge in orig_edge_matrix:
        try:
            test = g.get_eid(vertice_ids[orig_edge[0]],
                             vertice_ids[orig_edge[1]])
        except:
            print(f'Edges renaming test failed - edge {orig_edge} is missing')
            return False
    print('Edges renaming test passed!')
    return True


print(f'Edge count is correct: {len(df) == len(g.es)}')
print(f'Vertice count is correct: {len(vertices_unique) == len(g.vs)}')
print(test_edge_renaming())

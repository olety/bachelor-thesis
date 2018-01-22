# Finding communities
# Partitioning the large graph using louvain
partition = louvain.find_partition(g, louvain.ModularityVertexPartition)
louvain_graph = partition.cluster_graph()
ig.summary(louvain_graph)

# Partitioning the louvain graph using infomap
imap = louvain_graph.community_infomap()
ig.summary(imap)

# Saving the new graphs to pickle objects
with open('louvain_graph.pickle', 'wb') as f:
    pickle.dump(louvain_graph, f)
with open('imap.pickle', 'wb') as f:
    pickle.dump(imap, f)

# Following lines can be used to retrieve the saved files on the following runs
# with open('louvain_graph.pickle', 'rb') as f:
#     louvain_graph=pickle.load(f)
# with open('imap.pickle', 'rb') as f:
#     imap = pickle.load(f)

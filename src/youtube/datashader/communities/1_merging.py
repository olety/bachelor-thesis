lv_df_comm = pd.DataFrame({'name': louvain_graph.vs.indices,
                           'comm': imap.membership})
lv_df_comm.comm = lv_df_comm.comm.astype('category')
# ~2000 communities only have 1 member
print(lv_df_comm.comm.value_counts()[:15])

# Preparing the necessary lists
# Keep all communities with more than one member
comms_to_keep = [ind for ind, val
                 in enumerate(lv_df_comm.comm.value_counts())
                 if val > 1]

# len(...) is one more than the max value, since comms_to_keep starts with 0
# Create a new community for uncategorized
new_community_id = len(comms_to_keep)

# A list that will be used to replace the current community column
new_comms = []

for comm in lv_df_comm.comm:
    if comm in comms_to_keep:
        new_comms.append(comm)
    else:
        new_comms.append(new_community_id)

# Assigning it to to the df
lv_df_comm.comm = pd.Series(new_comms, dtype='category')

# Plotting the new category distribution
lv_df_comm.comm.value_counts().plot('bar')
plt.show()

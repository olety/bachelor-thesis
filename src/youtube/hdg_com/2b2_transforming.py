new_communities = hdg_imap[:7]
new_communities.append([j for i in hdg_imap[7:] for j in i])

new_membership = np.zeros(len(hdg_membership), dtype=int)
for ind in range(len(new_membership)):
    for comm in range(1, len(new_communities)):
        if ind in new_communities[comm]:
            new_membership[ind] = comm
            break

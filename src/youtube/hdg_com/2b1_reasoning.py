communities = [i for i in hdg_imap]
getlen = np.vectorize(lambda x: len(x))
pd.Series(getlen(communities)).plot.bar()
plt.show()

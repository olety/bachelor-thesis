df = df.map_partitions(transform)
df_comp = df.compute()

print(len(df) == len(df_comp))  # Prints True

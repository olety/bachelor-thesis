print(df.columns)  # Has duplicate columns due to joining
df = df.T.drop_duplicates().T  # Removing duplicate columns
df = df.infer_objects()  # Properly parse object types

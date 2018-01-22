def list_csv(path):
    for f in os.listdir(path):
        if f.endswith('.csv'):
            yield f

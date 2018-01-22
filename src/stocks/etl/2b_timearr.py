def get_timearr(stock_dir, example_timefile='A.csv'):
    time_df = pd.read_csv(os.path.join(
        stock_dir, example_timefile), index_col=0)
    return time_df.index.values

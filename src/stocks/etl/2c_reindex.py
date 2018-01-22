def reindex_csv(stock_dir, save_dir, time_arr, reload_data=False):
    if not os.path.isdir(save_dir):
        os.makedirs(save_dir)

    for stock_fname in tqdm(list_csv(stock_dir)):
        if not reload_data and os.path.isfile(os.path.join(save_dir,
                                                           stock_fname)):
            continue
        stock = pd.read_csv(os.path.join(stock_dir, stock_fname), index_col=0)
        stock = stock.reindex(time_arr, fill_value=np.nan)
        stock.to_csv(os.path.join(save_dir, stock_fname))
    gc.collect()

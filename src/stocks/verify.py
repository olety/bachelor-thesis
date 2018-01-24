# Check that all stocks have been merged
merged = merge_dfs(STOCK_FOLDER, MERGED_FOLDER, reload_data=True)
print(len(os.listdir('stocks/')) == merged.shape[1] / 4)  # Returns true

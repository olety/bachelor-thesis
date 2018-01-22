

def make_corr_matrix(merge_folder, save_folder,
                     merged_close_fname='stocks_close_merged.csv',
                     save_fname='corr_matrix.csv', reload_data=False):
    if (os.path.isfile(os.path.join(save_folder, save_fname)) and
            not reload_data):
        logging.warning('The target file is already present in the save_folder.'
                        ' Please use the reload_data argument to overwrite it.')
        return

    merged_path = os.path.join(merge_folder, merged_close_fname)
    save_path = os.path.join(save_folder, save_fname)

    logging.debug(f'Opening the merged closes folder at {merged_path}')
    merged_df = pd.read_csv(merged_path)
    corr_df = merged_df.corr()

    logging.debug(f'Saving the corr_df to {save_path}')
    corr_df.to_csv(save_path)

    return corr_df

pca = None
with open('pca.pickle', 'rb') as f:
    pca = pickle.load(f)

logging.info('Splitting the data into train and test '
             'datasets as well as converting it to the correct format')
X_train, y_train, X_test, y_test, pca, scaler = split_x_y(
    df_merged, do_pca=False, pca=pca)
logging.info('Finished data preprocessing')

# Uncomment if you want to save a newly generated PCA object
# logging.info('Saving the PCA object...')
# with open('pca.pickle', 'wb') as f:
#     pickle.dump(pca, f)
# logging.info('Finished saving the pca object')

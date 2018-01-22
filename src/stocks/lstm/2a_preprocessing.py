
def scale_series(col):
    return (col - col.min()) / (col.max() - col.min())


def convert_series(df_merged, window=30, pred_column='A', do_pca=False, pca=None, feature_len=None):
    X = []
    y = []
    col_number = df_merged.columns.get_loc('A')

    logging.info('Starting scaling...')
    scaler = MinMaxScaler(feature_range=(0, 1))
    data_scaled = scaler.fit_transform(df_merged.as_matrix())
    logging.info('Finished scaling')

    data_y = data_scaled[:, col_number]
    data_X = data_scaled

    # Doing the princomp analysis to reduce dims
    if do_pca:
        if pca is None:
            logging.info('Executing PCA...')
            pca = PCA(feature_len)
            pca.fit(data_X)
        data_X = pca.transform(data_X)

    logging.info(f'Number of features: {data_X.shape[1]}')

    # Processing X, y
    logging.info('Making X, y datasets')
    range_index = range(data_X.shape[0] - window - 1)
    for i in range_index:
        X.append(data_X[i: i + window])
        y.extend(data_y[i + window: i + window + 1])

    X = np.stack(X)
    y = np.array(y)
    return X, y, pca, scaler


def split_x_y(df, pred_column='A', window=30, test_rows=260, do_pca=False, pca=None, feature_len=None):
    # Converting the dataframe to something we can feed NN with
    logging.info('Converting dataframe to X,y')
    X, y, pca, scaler = convert_series(
        df, window, pred_column, do_pca, pca, feature_len)
    # Splitting the datasets
    logging.info('Splitting X,y into train and test datasets')
    X_train = X[:-test_rows]
    y_train = y[:-test_rows]
    X_test = X[-test_rows:]
    y_test = y[-test_rows:]
    return X_train, y_train, X_test, y_test, pca, scaler

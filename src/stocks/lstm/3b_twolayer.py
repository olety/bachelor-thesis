def make_two_layer_lstm(first_layer=1000, second_layer=200):
    # input shape = (nb_samples,timesteps =30, input_dim= cols)
    logging.info(f'Making a 2-layer model, l1={first_layer}, l2={second_layer}')
    model = Sequential()
    # Input layer
    logging.info('Processing input layer and hidden layer #1...')
    model.add(LSTM(
        first_layer,
        return_sequences=True,
        input_shape=(X_train.shape[1], X_train.shape[2]),  # X_train.shape[1]
        dropout=0.1
    ))
    # Hidden layer #1
    logging.info('Processing hidden layer #2...')
    model.add(LSTM(
        second_layer,
        return_sequences=False,
        dropout=0.2
    ))
    # Output layer
    logging.info('Processing output layer...')
    model.add(Dense(
        1,
        activation='linear'
    ))
    logging.info('Finished making the model')
    # Compiling the model
    logging.info('Started compilation...')
    start_time = time.time()
    model.compile(loss='mse', optimizer='adam')
    logging.info('Compiled in {}s'.format(time.time() - start_time))
    return model

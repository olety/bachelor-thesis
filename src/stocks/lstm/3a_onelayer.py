def make_one_layer_lstm(num_neurons=2000):
    # input shape = (nb_samples,timesteps =30, input_dim= cols)
    logging.info(
        'Started making one-layer model with {num_neurons} lstm cells...')
    model = Sequential()

    # Input layer
    logging.info('Processing input layer and hidden layer #1...')
    model.add(LSTM(
        num_neurons,
        return_sequences=False,
        input_shape=(X_train.shape[1], X_train.shape[2]),  # X_train.shape[1]
        dropout=0.1
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

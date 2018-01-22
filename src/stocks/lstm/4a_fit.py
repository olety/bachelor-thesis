for model_fun in [make_one_layer_lstm, make_two_layer_lstm]:
    model = model_fun()
    logging.info('Current model:')
    SVG(model_to_dot(model, show_shapes=True).create(prog='dot', format='svg'))
    model.save_weights('test_weights.h5')
    for epoch_size in [200]:
        # Stop if we haven't improved for X epochs
        model.load_weights('test_weights.h5')

        early_stopping_monitor = EarlyStopping(monitor='val_loss', patience=3)

        model.fit(
            X_train,
            y_train,
            batch_size=30,
            epochs=epoch_size,
            validation_split=0.1,
            shuffle=True,
            callbacks=[early_stopping_monitor]
        )

        model.evaluate(X_test, y_test)

        y_pred = predict_sequences_multiple(model, X_test, 30, 30)
        plot_results_multiple(y_pred, y_test, 30)
        plot_pred(model, X_test, y_test)
        model.save(f'{model_fun.__name__}_e{epoch_size}.h5')

models = [i for i in os.listdir() if '.h5' in i and 'weight' not in i]
for i in models:
    plot_pred(load_model(i), X_test, y_test)

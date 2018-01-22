for model_fun in [make_one_layer_lstm, make_two_layer_lstm]:
    model = model_fun()
    # Stop if we haven't improved for X epochs
    early_stopping_monitor = EarlyStopping(monitor='val_loss', patience=5)
    # Fit the model
    model.fit(
        X_train,
        y_train,
        batch_size=30,
        epochs=200,  # We can make it so large due to the early stopping monitor
        validation_split=0.1,
        shuffle=True,
        callbacks=[early_stopping_monitor]
    )
    # Print the loss on the test set
    model.evaluate(X_test, y_test)  # Will use the default scalar loss metric
    # Plot the prediction for the test set
    plot_pred(model, X_test, y_test)
    plt.show()
    # Save the model to a HDF5 file
    model.save(f'{model_fun.__name__}_e{epoch_size}.h5')

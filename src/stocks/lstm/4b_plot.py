def plot_pred(model, X_test, y_test):
    fig = plt.figure()  # Create a new figure
    plt.plot(y_test, label='True data')  # Plot the real data
    y_pred = model.predict(X_test)  # Predict the data using the X_test
    plt.plot(y_pred, label='Prediction')  # Plot the prediction
    plt.legend(fancybox=True, shadow=False)  # Add a legend to the plot
    return fig

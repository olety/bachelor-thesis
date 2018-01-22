def predict_sequences_multiple(model, data, window_size, prediction_len):
    # Predict sequence of 50 steps before shifting prediction run forward by 50 steps
    prediction_seqs = []
    for i in range(len(data) // prediction_len):
        curr_frame = data[i * prediction_len]
        predicted = []
        for j in range(prediction_len):
            predicted.append(model.predict(curr_frame[np.newaxis, :, :])[0, 0])
            curr_frame = curr_frame[1:]
            curr_frame = np.insert(
                curr_frame, [window_size - 1], predicted[-1], axis=0)
        prediction_seqs.append(predicted)
    return prediction_seqs


def plot_results_multiple(predicted_data, true_data, prediction_len):
    fig = plt.figure(facecolor='white')
    ax = fig.add_subplot(111)
    ax.plot(true_data, label='True Data')
    # Pad the list of predictions to shift it in the graph to it's correct start
    for i, data in enumerate(predicted_data):
        padding = [None for p in range(i * prediction_len)]
        plt.plot(padding + data, label='Prediction')
#     plt.title(f'MIDL {mid_lyr} EP{epochs} BTCH{batches}')
    plt.legend()
#     if not os.path.exists('plots'):
#         os.makedirs('plots')
#     plt.savefig(f'plots/ml{mid_lyr}_b{batches}_e{epochs}.png')
    plt.show()


def plot_pred(model, X_test, y_test):
    fig = plt.figure()
    _ = plt.plot(y_test, label='True data')
    y_pred = model.predict(X_test)
    _ = plt.plot(y_pred, label=f'Prediction')
    _ = plt.legend(fancybox=True, shadow=False)
    plt.show()

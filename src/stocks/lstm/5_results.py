# Get all model files in a directory
models = [i for i in os.listdir() if i.endswith('.h5')]
for i in models:
    temp_model = load_model(i)
    # Plotting the model's structure
    plot_model(temp_model, to_file=f'{i}.pdf', show_shapes=True)
    # Will use the default scalar loss metric
    print(i, temp_model.evaluate(X_test, y_test))
    plot_pred(temp_model, X_test, y_test)  # Plotting the model's prediction
    plt.savefig(f'prediction_{i}.pdf')  # Saving the prediction plot

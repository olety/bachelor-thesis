# Saving the images
for plot in tqdm(lv_plots, file=sys.stdout, desc='Plots saves:', unit='plot'):
    _ = ds.utils.export_image(plot, f'{plot.name}', fmt='.png')

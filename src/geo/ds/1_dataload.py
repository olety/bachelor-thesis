df = dd.read_csv(os.path.join(get_root(), 'taxi', 'Taxi_Trips.csv'), usecols=[
    'Trip Start Timestamp',
    'Trip End Timestamp',
    'Trip Seconds',
    'Trip Miles',
    'Trip Total',
    'Payment Type',
    'Pickup Centroid Location',
    'Dropoff Centroid  Location'
], assume_missing=True).dropna().reset_index(drop=True)
df = df.rename(columns={'Dropoff Centroid  Location': 'Dropoff',
                        'Pickup Centroid Location': 'Pickup'})

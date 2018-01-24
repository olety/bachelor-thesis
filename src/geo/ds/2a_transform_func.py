def convert_points(arr):
    return_list = []
    for point in arr:
        try:
            # If we can't parse the float, the row is empty, fill it with 0s
            return_list.append([float(var) for var in point[7:-1].split(' ')])
        except:
            return_list.append([0.0, 0.0])
    return return_list


def transform(df):
    # Pickup
    # Converting the pickup column into numbers
    pickup_latlng = pd.DataFrame(convert_points(df['Pickup']),
                                 columns=['pickup_x', 'pickup_y'])
    # Converting lat/lng to Mercator coords
    df['pickup_x'], df['pickup_y'] = lnglat_to_meters(
        pickup_latlng['pickup_x'], pickup_latlng['pickup_y'])

    # Dropoff
    dropoff_latlng = pd.DataFrame(convert_points(df['Dropoff']),
                                  columns=['dropoff_x', 'dropoff_y'])
    df['dropoff_x'], df['dropoff_y'] = lnglat_to_meters(
        dropoff_latlng['dropoff_x'], dropoff_latlng['dropoff_y'])

    return df

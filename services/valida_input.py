def is_valid_lat_lon(x: str):
    parts = x.split(',')
    if len(parts) == 2:
        try:
            lat = float(parts[0].strip())
            lng = float(parts[1].strip())
            return lat, lng
        except ValueError:
            return False
    return False
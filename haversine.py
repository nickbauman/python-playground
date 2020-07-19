import math


def haversine(lat1, lon1, lat2, lon2):
    """
    Calculate the great circle distance (in meters) between two points on the earth specified in decimal degrees,
    (lon1, lat1) and (lon2, lat2).

    :param lon1: The first longitude value, in decimal degrees.
    :param lat1: the first latitude value, in decimal degrees.
    :param lon2: The second longitude value, in decimal degrees.
    :param lat2: The second latitude value, in decimal degrees.
    :return: The distance between (lon1, lat1) and (lon2, lat2) in meters.
    """
    lon1, lat1, lon2, lat2 = map(math.radians, [lon1, lat1, lon2, lat2])

    print("lon1", lon1)
    print("lat1", lat1)
    print("lon2", lon2)
    print("lat2", lat2)

    # haversine formula
    lng = lon2 - lon1
    lat = lat2 - lat1
    print("lng", lng)
    print("lat", lat)

    a = math.sin(lat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(lng / 2) ** 2
    c = 2 * math.asin(math.sqrt(a))
    r = 6371.0088  # 6371 km is the radius of the Earth
    print("a", a)
    print("c", c)
    return (c * r) * 1000  # meters


paris = [48.8566, 2.3522]
lyon = [45.7640, 4.8357]

haversine(paris[0], paris[1], lyon[0], lyon[1])

# Importing the geodesic module from the library
from geopy.distance import geodesic
from geopy.geocoders import Nominatim

def getDistance(list, coords):

    latitude = float(list[2][1:-1])
    longitude = float(list[3][1:-1])

    return geodesic((latitude,longitude), coords).km

def convertAddress(address):
    # catch errors

    geolocator = Nominatim(user_agent="TakeTheWheel")
    location = geolocator.geocode(address)
    return (location.latitude, location.longitude)


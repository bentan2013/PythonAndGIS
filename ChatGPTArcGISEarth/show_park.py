
import pandas as pd
from geopy.geocoders import Nominatim
import geocoder

# create geocoder object
geolocator = Nominatim(user_agent="my-app")

# list of park names in Los Angeles
parknames = [
    "Griffith Park",
    "Runyon Canyon Park",
    "Echo Park",
    "Exposition Park",
    "MacArthur Park",
    "Los Angeles State Historic Park",
    "Grand Park",
    "Hancock Park",
    "Cheviot Hills Park",
    "Elysian Park",
    "Kenneth Hahn State Recreation Area",
    "Barnsdall Art Park",
    "Lake Balboa Park",
    "Stough Canyon Nature Center",
    "Will Rogers State Historic Park",
    "Whittier Narrows Recreation Area",
    "Wattles Garden Park",
    "El Cariso Community Regional Park",
    "Westwood Recreation Center",
    "Chatsworth Park South",
    "Palisades Park",
    "Franklin Canyon Park",
    "Ernest E. Debs Regional Park",
    "Sepulveda Basin Recreation Area",
    "Westridge-Canyonback Wilderness Park"
]

# create empty lists for latitude and longitude
addresses = []
latitudes = []
longitudes = []

def get_lon_lat(address):
    g = geocoder.arcgis(address)
    rlt = g.json
    if "lng" in rlt:
        return rlt["lng"], rlt["lat"]
    else:
        return 0.0, 0.0

# loop through park names to get latitude and longitude for each
for parkname in parknames:
    address = parkname + ", Los Angeles, CA"
    lon, lat = get_lon_lat(address)
    #location = geolocator.geocode(address)
    #if location:
    #    addresses.append(parkname)  
    #    latitudes.append(location.latitude)
    #    longitudes.append(location.longitude)
    addresses.append(parkname)  
    latitudes.append(lat)
    longitudes.append(lon)

# create dataframe with park names, latitudes, and longitudes
df = pd.DataFrame({
    "park": addresses,
    "latitude": latitudes,
    "longitude": longitudes
})

# export dataframe to json
jsons = df.to_json()
print(jsons)

import json
from earth_api import EarthAPI
earth = EarthAPI()

#load parks json to dict
parks = json.loads(s=jsons)

def generate_drawings_from_point(name, lat, lon):
    place_marker = {
        "visible": True,
        "title": name,
        "geometry": {
            "x": lon,
            "y": lat,
            "spatialReference": {"wkid": 4326}
            },
        "symbol": {
            "type": "picture-marker",
            "url":"https://static.arcgis.com/images/Symbols/Shapes/BlackStarLargeB.png",
            "size": "64px"
        },
        "labelSymbol":{
            "type":"text",
            "color": [255,255,255,255],
            "size":12
        }
    }
    return place_marker

for i in range(len(parks['park'])):
    name = parks['park'][str(i)]
    lat = parks['latitude'][str(i)]
    lon = parks['longitude'][str(i)]
    drawing = generate_drawings_from_point(name, lat, lon)
    earth.add_drawing(drawing)
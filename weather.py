import requests
import geocoder

# Returns a json of the weather data such as temperature, sky, humidity, wind, etc.
def get_json_weather_data_From_lat_lon(lat, lon, api_key):
    api_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
    return requests.get(url=api_url).json()



# Main starts here
g = geocoder.ip('me')
#print(get_json_weather_data_From_lat_lon(g.latlng[0], g.latlng[1], api_key)['weather'])

#print(g.latlng)
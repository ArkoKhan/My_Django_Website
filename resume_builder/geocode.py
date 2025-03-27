

from password import GEOCODE_API_KEY
import requests



class GeoCode:
    def __init__(self):
        self.endpoint = "https://geocode.maps.co/search"
        self.endpoint_rev = "https://geocode.maps.co/reverse"

    def forward(self, query):
        params = {
            "q": query,
            "api_key": GEOCODE_API_KEY
        }
        response = requests.get(self.endpoint, params=params)
        data_res = response.json()[0]
        dict_res = {
            "location": data_res["display_name"],
            "lat": data_res["lat"],
            "lon": data_res["lon"]
        }
        return dict_res

    def reverse(self, lat, lon):
        params = {
            "lat": lat,
            "lon": lon,
            "api_key": GEOCODE_API_KEY
        }
        response = requests.get(self.endpoint_rev, params=params)
        data_res = response.json()
        res_location = data_res["display_name"]
        return res_location


data = GeoCode()
print(data.reverse(23.8103, 90.4125))


# import requests


# def geocode(endereco):
#     api_url = 'https://nominatim.openstreetmap.org/search'
#     params = {'q': endereco, 'format': 'json', 'limit': 1}
#     response = requests.get(api_url, params=params)
#     if response.status_code == 200 and response.json():
#         resultado = response.json()[0]
#         latitude = float(resultado['lat'])
#         longitude = float(resultado['lon'])
#         return latitude, longitude
#     else:
#         raise ValueError('Endereço não encontrado')


import googlemaps
from config.settings import Settings

gmaps = googlemaps.Client(Settings().GEO_API_KEY)


def geocode(endereco):
    return gmaps.geocode(endereco)

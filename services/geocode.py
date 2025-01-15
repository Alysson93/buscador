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

gmaps = googlemaps.Client('')


def geocode(endereco):
    geocode_result = gmaps.geocode(endereco)
    if len(geocode_result) >= 1:
        latitude = geocode_result[0]['geometry']['location']['lat']
        longitude = geocode_result[0]['geometry']['location']['lng']
    else:
        latitude = 0
        longitude = 0
    return (latitude, longitude)

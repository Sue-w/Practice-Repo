import requests

# example request form:
# https://maps.googleapis.com/maps/api/geocode/outputFormat?parameters
# The API will place the response in a `results` array


def get_geocode(my_input):
    key = "TO_BE_GIVEN"
    BASE_URL = "https://maps.googleapis.com/maps/api/geocode/"
    address = my_input.replace(' ', '%20')
    address = address.replace(',', '%2C')
    requests.get(f"{BASE_URL}json?address={address}&key={key}")
    lat, long = results.json()[geometry][location]
    print(f"\nTokyo, Japan is {lat}, {long}")


coordinates = get_geocode("Tokyo, Japan")
print(coordinates)

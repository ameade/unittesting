import requests

def get_location():
    response = requests.get("https://ipvigilante.com")
    if response.status_code != 200:
        raise Exception("Received bad response from ipvigilante. %s" % response.raw)
    loc = response.json()['data']

    return loc["longitude"], loc["latitude"]

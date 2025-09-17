import json
import ssl
from urllib.request import urlopen
def main():
    url =  "https://api.weather.gov/points/40.1934,-85.3864"
    context = ssl._create_unverified_context
    response = urlopen(url, context=context)
    properties = json.loads(response.read())
    print(len(properties["features"]))
    for forecast in properties["features"]:
        print(forecast["name"]["temperature"]["detailedForecast"])

main()


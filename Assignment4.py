import json
import ssl
from urllib.request import urlopen
def main():
    url =  "https://api.weather.gov/points/40.1934,-85.3864"
    context = ssl._create_unverified_context()
    response1 = urlopen(url, context=context)
    data1 = json.load(response1)
    forcastURL = data1['properties']['forecast']
    response2 = urlopen(forcastURL, context=context)
    data2 = json.load(response2)
    for period in data2['properties']['periods']:
        print(f"Period: {period['name']}")
        print(f"Temperature: {period['temperature']}")
        print(f"Detailed Forecast {period['detailedForecast']}")

main()


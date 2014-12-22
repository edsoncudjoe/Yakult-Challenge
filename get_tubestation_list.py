# This is a tool to create a list of London underground stations

import requests
from bs4 import BeautifulSoup

url = "http://en.wikipedia.org/wiki/List_of_London_Underground_stations"
data = requests.get(url)

soup_data = BeautifulSoup(data.content)

alinks = soup_data.find_all('a')

cleaned = soup_data.find_all("th", {"scope": "row"})

with open("tubestations.txt", "w") as stations:
    for item in cleaned:
        stations.write(item.text + "\n")

import requests
import time
import folium

url = 'http://api.open-notify.org/iss-now.json'


def issPosition(url):
    r = requests.get(url).json()
    longitude = r["iss_position"]["longitude"]
    latitude = r["iss_position"]["latitude"]
    position = 'la longitude est ' + longitude, " la latitude est " + latitude
    print(position)
    return float(latitude), float(longitude)


# looping the search each few seconds
for i in range(5):
    latitude, longitude = issPosition(url)
    time.sleep(2)

# and where is ISS position on a world map now!
print(latitude, longitude)

m = folium.Map(location=[latitude, longitude],
               zoom_start=5, tiles='Stamen Terrain')

folium.Marker([latitude, longitude]).add_to(m)
m.save('position.html')

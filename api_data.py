
import json

'''
import requests
res = requests.get('https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m')

# res.text returns a plain text
# res.json() parse the json data into python object (dict, list of dict)

if res.status_code==200:
     res = res.json() # dict/obj
     # saving in a file in txt format
     with open('weather.json', 'w', encoding='utf-8') as f:
          data = json.dumps(res) # obj -> str
          f.write(data)
else:
     print(res.status_code)
'''

with open('weather.json', 'r', encoding='utf-8') as f:
     data = f.read()

res = json.loads(data) # str->obj
# print(res.keys())

lat = res['latitude']
lon = res['longitude']
elev = res['elevation']
curr = res['current']
temp = curr['temperature_2m']
wind_speed = curr['wind_speed_10m']

print("WEATHER REPORT")
print("-"*10)
print("latitude: ",lat)
print("longitude: ",lon)
print("elevation: ",elev)
print("temperature: ",temp, "deg C")
print("wind speed: ",wind_speed, "km/h")

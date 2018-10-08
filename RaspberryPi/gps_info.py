import urllib.request
import json

class GpsInfo:
    
    def __init__(self):
        self.name = 'unknown'
        self.latitude = 0.0
        self.longitude = 0.0

    def setName(self, name):
        self.name = name

    def setPosition(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def postGps(self, url):
        data = {
            'name': self.name,
            'latitude': self.latitude,
            'longitude': self.longitude
        }
        data_json = json.dumps(data).encode('utf8')

        request = urllib.request.Request(url, data_json, {'Content-Type' : 'application/json'})
        response = urllib.request.urlopen(request)

    def getGpsList(self, url):
        request = urllib.request.Request(url)
        response = urllib.request.urlopen(request)
        data_json = json.loads(response.read().decode('utf8'))

        for item in data_json:
            print(item['name'],item['latitude'],item['longitude'])
        
        return (data_json)
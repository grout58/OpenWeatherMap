import urllib.request
import json

class OpenWeather:
    def __init__(self, zip_code, country, units, api_key,cur_temp=None):
        self.units = units
        self.country = country
        self.zip_code = zip_code
        self.api_key = api_key
        self.cur_temp = cur_temp

    def get_data(self):
        with urllib.request.urlopen("http://api.openweathermap.org/data/2.5/weather?zip={},{}&appid={}&units={}".format(self.zip_code, self.country, self.api_key, self.units)) as url:
            data = json.loads(url.read().decode())
            for key, value in data.items():
                if key == 'main':
                    self.cur_temp = value['temp']

import urllib.request
import json

class OpenWeather:
    def __init__(self, zip_code, country, units, api_key,cur_temp=None,low_temp=None,high_temp=None,loc_name=None):
        self.units = units
        self.country = country
        self.zip_code = zip_code
        self.api_key = api_key
        self.cur_temp = cur_temp
        self.low_temp = low_temp
        self.high_temp = high_temp
        self.loc_name = loc_name

    def get_data(self):
        with urllib.request.urlopen("http://api.openweathermap.org/data/2.5/weather?zip={},{}&appid={}&units={}".format(self.zip_code, self.country, self.api_key, self.units)) as url:
            data = json.loads(url.read().decode())
            for key, value in data.items():
                if key == 'main':
                    self.cur_temp = value['temp']
                    self.low_temp = value['temp_min']
                    self.high_temp = value['temp_max']
                elif key == 'name':
                    self.loc_name = value

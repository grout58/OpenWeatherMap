import openweather

owo = openweather.OpenWeather('01844', 'us', 'imperial', '60b91248e90de082739c85e97bd85da9')

owo.get_data()
print(owo.cur_temp)
print(owo.low_temp)
print(owo.high_temp)
print(owo.loc_name)

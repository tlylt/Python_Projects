#!usr/bin/python3
# API used:https://sunrise-sunset.org/api

import requests
from dateutil.parser import parse
from dateutil.tz import tzlocal

API_URL = "https://api.sunrise-sunset.org/json?&formatted=0"
location = "&lat=1.3521&lng=103.8198"  # Singapore

response = requests.get(API_URL+location)
data = response.json()
print(data)
sunrise=data['results']['sunrise']
parsed_sr=parse(sunrise)
sg=tzlocal()
sunrise_info=parsed_sr.astimezone(sg)
print(sunrise_info)
# print("Checking for country: Singapore")
# print("[Today]\nSunrise time: {}\n Sunset time: {}\n Day duration: {}".format(**data['results']))

# To-DO
# from datetime import date, timedelta
# dates=[]
# for i in range(0, 365):
#     dates.append(date.today() + timedelta(i))
# for d in dates:
#     response = requests.get(API_URL+location+'&date={}'.format(d))
#     data=response.json()
#     print(data['results']['day_length'])

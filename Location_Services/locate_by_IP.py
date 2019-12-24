import requests

#using the service of ipinfo.io
url="https://ipinfo.io/json"

#getting the response and convert from json to dictionary
response = requests.get(url)
data=response.json()

#some facts
print("You are living in {city}.\nYour IP address is {ip}.".format(**data))
print("Your estimated location suggested by the IP address is {}E.".format(data['loc'].replace(',','N, ')))
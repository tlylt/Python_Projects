#!/usr/bin/python3

import re
import subprocess
import requests

# the geolocation service by Google, input your API key from Google APIs project credentials
API_url = "https://www.googleapis.com/geolocation/v1/geolocate?key="
API_key = "Your google api key"

# gather info for better accuracy
payload = {}
try:
    #gather network info
    cmdout = subprocess.check_output('netsh wlan show networks mode=bssid').decode(encoding='utf_8')
    macs = re.findall(r'(?:[0-9a-f-A-F]:?){12}',cmdout)
    signals = re.findall(r'([\d]+)%',cmdout)
    channels = re.findall(r'Channel[\W]+: ([\d]+)',cmdout)
except:
    print('Unable to get WiFi access points.')
else:
    print('Using {0} WiFi access point{1}'.format(len(macs),'s' if (len(macs) >1) else ''))
    wifi_l=[]
    for i in range(len(macs)):
        wifi_l.append({
            'macAddress':macs[i],
            'signalStrength':int(signals[i])/2 -100,
            'channel':int(channels[i])
        })
    payload['wifiAccessPoints'] = wifi_l

#make request to API
try:
    response = requests.post(API_url+API_key,json=payload)
    data = response.json()
    if 'error' in data.keys():
        raise requests.RequestException('Error {0}: {1}'.format(data['error']['code'],data['error']['message']))
except Exception as e:
    print(e)
else:
    lat=data['location']['lat']
    lng=data['location']['lng']
    accuracy=data['accuracy']
    print('You are within {0}m of {lat}N {lng}E'.format(accuracy,**data['location']))
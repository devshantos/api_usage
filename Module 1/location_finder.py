'''import requests
api_url = requests.get('https://api64.ipify.org?format=json')
responses = api_url
if responses.status_code == 200:
    calling_url = responses.json()
    calling_ip = calling_url.get('ip')

ip_location = requests.get(f'https://api.iplocation.net/?ip={calling_ip}')
if ip_location.status_code == 200:
    data = ip_location.json()
    ip = data.get('ip')
    ip_number = data.get('ip_number')
    ip_version = data.get('ip_version')
    country_name = data.get('country_name')
    article = f'This ip address is {ip}. His ip number {ip_number}. IP version is {ip_version}. This ip stay in {country_name}.'
    print(article)'''
import requests

import requests
api_url = requests.get('https://api.ipify.org?format=json')
res = api_url
if res.status_code == 200:
    calling_code = res.status_code
    calling_ip = res.json()


ip_location_url = f'https://api.iplocation.net/?ip={calling_ip}'


track = requests.get(ip_location_url)
if track.status_code == 200:
    full_details = track.text
    print(full_details)

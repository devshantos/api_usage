import requests
api_uri = requests.get('https://api.ipify.org?format=json')
responses = api_uri

if responses.status_code == 200:
    user_ip = responses.json()
    ip = user_ip.get('ip')
    print('You are seeing your ip addpress. Here are your ip address: ', ip)

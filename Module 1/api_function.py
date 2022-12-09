import requests
def return_data(url):
    api = requests.get(url)
    if api.status_code == 200:
        res = api.json()
    return res


api_find_url = ('https://api64.ipify.org?format=json')
response = return_data(api_find_url)
ip = response


api_user_location = requests.get(f'https://api.iplocation.net/?ip={ip}')

data = api_user_location.json()
ip_address = data.get('ip')
print(data)


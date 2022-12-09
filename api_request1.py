import requests
url = 'https://rapidapi.com/api-sports/api/api-football/'
api = requests.get(url)
responses = api.text
print(responses)
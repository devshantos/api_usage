import requests
responses = requests.get(' https://developer.amazonservices.com/ref=rm_5_sv')
print(responses.status_code)
print(responses.json())
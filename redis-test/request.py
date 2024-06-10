import requests

url = 'http://localhost:8000/send'
payload = {'message': 'Hello, world!'}
response = requests.post(url, json=payload)
print(response.json())

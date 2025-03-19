import requests

url = "https://api.coincap.io/v2/assets"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

cotacao = response.json()
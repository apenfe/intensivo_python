import requests
import json

url = "https://hacker-news.firebaseio.com/v0/item/31353677.json"
r = requests.get(url)
print(f"Status code: {r.status_code}")

response = r.json()
response_tring = json.dumps(response,indent=4)
print(response_tring)

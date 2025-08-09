import json

import requests


heads = {'Accept':'text/plain','Content-Type':'application/json',"x-api-key": "reqres-free-v1"}
base_url = "https://reqres.in/api/users"

json_file = open('./users.json')
json_payload = json.load(json_file)

response = requests.post(base_url,headers=heads,json=json_payload)
print((response.json()))
import requests

parameters = {
    'page': 1,
    'per_page':5
}
url = "https://gorest.co.in/public/v2/users"
resp = requests.get(url,params=parameters)
print(resp.json())
print(resp.status_code)
assert resp.status_code == 200
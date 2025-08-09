import requests

head = {
    "accept" : 'text/plain'
}
##GET request
response = requests.get("https://fakerestapi.azurewebsites.net/api/v1/Activities/9",headers=head)
print(response.status_code)
print(response.json())

assert response.status_code == 200
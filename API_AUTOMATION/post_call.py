import requests

header = {
    "Accept":'text/plain',
    "Content-Type":'application/json'
}
request_payload = {
    "id": 193,
    "idBook": 123,
    "firstName": "REST API",
    "lastName": "TESTING"
}

resp = requests.post("https://fakerestapi.azurewebsites.net/api/v1/Authors",headers=header,json=request_payload)
print(resp.status_code)
print(resp.json())

data = resp.json()
print(data['id'])
assert resp.status_code == 200
assert data['firstName'] == 'REST API'
import requests


print("Get the data before update")

head = {
    "Accept": "text/plain"
}
response = requests.get("https://fakerestapi.azurewebsites.net/api/v1/Activities/12",headers=head)
print(response.json())


print("Data after updating using the PUT Request")
##add the headers
header = {
    "Accept": "text/plain",
    "Content-Type": "application/json"
}
## Add the payload to update the data
put_payload = {
    "id": 15,
    "title": "PUT API Testing",
    'dueDate': '2025-08-10T03:49:32.7129628+00:00',
    "completed": False
}
resp = requests.put("https://fakerestapi.azurewebsites.net/api/v1/Activities/12",headers=header,json=put_payload)
print(resp.status_code)
print(resp.json())
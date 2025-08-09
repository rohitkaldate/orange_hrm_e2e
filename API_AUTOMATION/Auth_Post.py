import requests
from urllib3 import request

head = {
    'Accept': 'text/plain',
    'Content-Type':'application/json',
    'Authorization': 'Bearer 44203d3065afef8e926edbb957e5098a274fe5c45394cf85cabc1524904fc04d '
}

request_body = {
    "name": "Chitradip 123",
    "email": "jain_chitra1234@gmail.com",
    "gender": "male",
    "status": "active"
}
url = "https://gorest.co.in/public/v2/users"
auth_post_resp = requests.post(url,headers=head,json=request_body)
print(auth_post_resp.json())
print(auth_post_resp.status_code)


get_resp = requests.get(url+'/'+str(auth_post_resp.json()['id']),headers=head)
print(get_resp.json())
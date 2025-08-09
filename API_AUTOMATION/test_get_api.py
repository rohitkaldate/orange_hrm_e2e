import requests

def test_get_validation():
    head ={
        'Content-Type':'application/json',
        "x-api-key": "reqres-free-v1"
    }
    base_url = 'https://reqres.in'
    resp = requests.get(base_url+'/api/users/2',headers=head)
    print(resp.text)
    assert 200 == resp.status_code
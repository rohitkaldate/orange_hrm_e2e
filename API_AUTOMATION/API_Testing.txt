****************** This is about the API Testing using the selenium ********************************

*** To use the API in the testing we need import the requests library first and then only we can able to test the api testing ***

## GET Request :
    Get is use to fetch the response.
    It will give the response associated with the request.
    To work with the get request we need to use the get call from the requests library for the particular URL.
    Example:
        head = {
            "accept" : 'text/plain'
        }
        resp = request.get("URL",headers=head)
        print(resp.status.code)
        print(resp.json())

## POST Request:
     POST is used to create/add/insert the new information/data in the already existing information.
     To work with the the POST request we need to import the requests library and from that we need to call the POST method.
     But while working on the POST we need to add the PAYLOAD/JSON data into it,then it will be created/inserted/added into the dataset.
     Make sure the payload must be in the form of JSON.

     Example:

        header = {
            "Accept" : 'text/plain',
            "Content-Type":'Application/json'
        }

        request_payload = {
            "id": 193,
            "idBook": 123,
            "firstName": "REST API",
            "lastName": "TESTING"
        }

        resp = requests.post("URL",headers=header,json=request_payload)
        print(resp.status.code)
        print(resp.json())


## PUT Request:
    It will used to update the existing data.
    This method will first check if the data is already present or not and if present then it will update that only.

    Example:
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

## Authorization:
    It is like who can access what things.
    If I knows someone is authentication but that doesn't mean that someone have all the access which I have.

## Pass parameter in the URL is nothing but the filtering the data present on the web.
    params used to pass the parameters in the url

## Pass the JSON data using the .json file instead of the payload:
    Example:
        import json
        import requests

        heads = {'Accept':'text/plain','Content-Type':'application/json',"x-api-key": "reqres-free-v1"}
        base_url = "https://reqres.in/api/users"

        json_file = open('./users.json')   ## call the users.json file from the directory
        json_payload = json.load(json_file)

        response = requests.post(base_url,headers=heads,json=json_payload)
        print((response.json()))

## API With the PyTest Framework

    Example:
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
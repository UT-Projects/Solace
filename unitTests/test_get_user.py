import requests
import json

url = "http://localhost:3000/"

class TestGetUser:
    def test_gu_basic_1(self):
        params = {
            "uuid": "510d2b66-b86a-4271-b175-c127e6c19e53"
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url + "getUser", params=params, headers=headers)
        print(response.text)
        assert response.status_code == 200
        assert response.ok
        assert json.loads(response.content.decode())["Item"]["name"] == "Samuel Menist"

    def test_gu_basic_2(self):
        params = {
            "uuid": "76969fee-b50c-49fc-8b65-3a8770bc05ec"
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url + "getUser", params=params, headers=headers)
        print(response.text)
        assert response.status_code == 200
        assert response.ok
        assert json.loads(response.content.decode())["Item"]["email"] == "brianisabigboy14@yahoo.com"

    def test_gu_invalid_1(self):
        params = {
            "uuid": "76969fee-b50c-49fc-8b65-3a8770bc05ed"
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url + "getUser", params=params, headers=headers)
        print(response.text)
        assert response.status_code == 200
        assert response.text == "{}"
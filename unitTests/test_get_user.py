import requests
import json

url = "http://localhost:3000/"

"""
('510d2b66-b86a-4271-b175-c127e6c19e53', 'Samuel Menist', 1128834000, 'female', 'sami@gmail.com'),
('76969fee-b50c-49fc-8b65-3a8770bc05ec', 'Brian Chugg', 354949200, 'female', 'brianisabigboy14@yahoo.com'),
"uuid": user[0],
"name": user[1],
"birthdate": user[2],
"sex": user[3],
"email": user[4]
"""

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
        user = json.loads(response.content.decode())["Item"]
        assert user["name"] == "Samuel Menist"
        assert user["birthdate"] == 1128834000
        assert user["sex"] == 'female'
        assert user["email"] == 'sami@gmail.com'

    def test_gu_basic_2(self):
        params = {
            "uuid": "76969fee-b50c-49fc-8b65-3a8770bc05ec"
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url + "getUser", params=params, headers=headers)
        print(response.text)
        assert response.status_code == 200
        assert response.ok
        user = json.loads(response.content.decode())["Item"]
        assert user["name"] == 'Brian Chugg'
        assert user["birthdate"] == 354949200
        assert user["sex"] == 'female'
        assert user["email"] == "brianisabigboy14@yahoo.com"

    def test_gu_invalid_1(self):
        params = {
            "uuid": "76969fee-b50c-49fc-8b65-3a8770bc05ed"
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url + "getUser", params=params, headers=headers)
        print(response.text)
        assert response.status_code == 200
        assert response.text == "{}"
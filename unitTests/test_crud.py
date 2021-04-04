import requests
import json


url = "http://localhost:3000/"

class TestCreateUser:
    def test_basic(self):
        payload = {
            "uuid": "1171737d-fb41-453f-87b4-6463c890347d",
            "name": "Big Chungas",
            "birthdate": 1322719200.0,
            "sex": "male",
            "email": "chug@fatbasterd.com"            
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url + "createUser", data=json.dumps(payload), headers=headers)
        print(response.text)
        assert response.status_code == 200

class TestGetUser:
    def test_basic(self):
        pass        


class TestUpdateUser:
    def test_basic(self):
        pass


class TestDeleteUser:
    def test_basic(self):
        pass

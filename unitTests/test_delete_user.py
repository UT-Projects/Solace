import requests
import json

url = "http://localhost:3000/"

class TestDeleteUser:
    def test_basic_1(self):
        headers = {'Content-Type': 'application/json'}
        response = requests.delete(url + "deleteUser?uuid=2d99ce89-d882-4578-a75c-024c099b1d24", headers=headers)
        print(response.text)
        assert response.status_code == 200
        assert response.ok

        response = requests.get(url + "getUser?uuid=2d99ce89-d882-4578-a75c-024c099b1d24", headers=headers)
        result = response.json()
        assert not result


    def test_basic_2(self):
        headers = {'Content-Type': 'application/json'}
        response = requests.delete(url + "deleteUser?uuid=1e0dc55a-1de1-4349-86a3-089da3cde919", headers=headers)
        print(response.text)
        assert response.status_code == 200
        assert response.ok

        response = requests.get(url + "getUser?uuid=1e0dc55a-1de1-4349-86a3-089da3cde919", headers=headers)
        result = response.json()
        assert not result

    def test_basic_3(self):
        headers = {'Content-Type': 'application/json'}
        response = requests.delete(url + "deleteUser?uuid=7cb19016-1343-4226-8b59-89dd079be6e6", headers=headers)
        print(response.text)
        assert response.status_code == 200
        assert response.ok

        response = requests.get(url + "getUser?uuid=7cb19016-1343-4226-8b59-89dd079be6e6", headers=headers)
        result = response.json()
        assert not result

    def test_basic_4(self):
        headers = {'Content-Type': 'application/json'}
        response = requests.delete(url + "deleteUser?uuid=8be74c06-9657-44c6-9ede-4424a698e3e3", headers=headers)
        print(response.text)
        assert response.status_code == 200
        assert response.ok

        response = requests.get(url + "getUser?uuid=8be74c06-9657-44c6-9ede-4424a698e3e3", headers=headers)
        result = response.json()
        assert not result
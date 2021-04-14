import requests
import json

url = "http://localhost:3000/"

class TestUpdateUser:
    def test_name_1(self):
        payload = {
            "uuid": "21843d4c-51bb-4d85-a066-75047d19086b",
            "key": "name",
            "value": "Steven Bonk"
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.put(url + "updateUser", data=json.dumps(payload), headers=headers)
        print(response.text)
        assert response.status_code == 200
        assert response.ok

        response = requests.get(url + "getUser?uuid=21843d4c-51bb-4d85-a066-75047d19086b", data=json.dumps(payload), headers=headers)
        result = response.json()
        print(result["Item"]["name"] == "Steven Bonk")

    def test_name_2(self):
        payload = {
            "uuid": "21843d4c-51bb-4d85-a066-75047d19086b",
            "key": "name",
            "value": "Steven Bak"
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.put(url + "updateUser", data=json.dumps(payload), headers=headers)
        print(response.text)
        assert response.status_code == 200
        assert response.ok

        response = requests.get(url + "getUser?uuid=21843d4c-51bb-4d85-a066-75047d19086b", data=json.dumps(payload), headers=headers)
        result = response.json()
        print(result["Item"]["name"] == "Steven Bak")

    def test_birthdate_1(self):
        payload = {
            "uuid": "ebdd8907-65b8-46e4-a714-f0c15ab450f2",
            "key": "birthdate",
            "value": 249199201.0
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.put(url + "updateUser", data=json.dumps(payload), headers=headers)
        print(response.text)
        assert response.status_code == 200
        assert response.ok

        response = requests.get(url + "getUser?uuid=ebdd8907-65b8-46e4-a714-f0c15ab450f2", data=json.dumps(payload), headers=headers)
        result = response.json()
        print(result["Item"]["birthdate"] == 249199201.0)

    def test_birthdate_2(self):
        payload = {
            "uuid": "ebdd8907-65b8-46e4-a714-f0c15ab450f2",
            "key": "birthdate",
            "value": 249199200.0
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.put(url + "updateUser", data=json.dumps(payload), headers=headers)
        print(response.text)
        assert response.status_code == 200
        assert response.ok

        response = requests.get(url + "getUser?uuid=ebdd8907-65b8-46e4-a714-f0c15ab450f2", data=json.dumps(payload), headers=headers)
        result = response.json()
        print(result["Item"]["birthdate"] == 249199200.0)

    def test_sex_1(self):
        payload = {
            "uuid": "bef6c25e-a162-472d-ae7f-7b7ab6c42b31",
            "key": "sex",
            "value": "male"
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.put(url + "updateUser", data=json.dumps(payload), headers=headers)
        print(response.text)
        assert response.status_code == 200
        assert response.ok

        response = requests.get(url + "getUser?uuid=bef6c25e-a162-472d-ae7f-7b7ab6c42b31", data=json.dumps(payload), headers=headers)
        result = response.json()
        print(result["Item"]["sex"] == "male")

    def test_sex_2(self):
        payload = {
            "uuid": "bef6c25e-a162-472d-ae7f-7b7ab6c42b31",
            "key": "sex",
            "value": "female"
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.put(url + "updateUser", data=json.dumps(payload), headers=headers)
        print(response.text)
        assert response.status_code == 200
        assert response.ok

        response = requests.get(url + "getUser?uuid=bef6c25e-a162-472d-ae7f-7b7ab6c42b31", data=json.dumps(payload), headers=headers)
        result = response.json()
        print(result["Item"]["sex"] == "female")

    def test_email_1(self):
        payload = {
            "uuid": "e820ce78-9499-41f2-84ef-1da35946240b",
            "key": "email",
            "value": "elfriedaroudebushloveschicken@gmail.com"
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.put(url + "updateUser", data=json.dumps(payload), headers=headers)
        print(response.text)
        assert response.status_code == 200
        assert response.ok

        response = requests.get(url + "getUser?uuid=e820ce78-9499-41f2-84ef-1da35946240b", data=json.dumps(payload), headers=headers)
        result = response.json()
        print(result["Item"]["email"] == "elfriedaroudebushloveschicken@gmail.com")

    def test_email_2(self):
        payload = {
            "uuid": "e820ce78-9499-41f2-84ef-1da35946240b",
            "key": "email",
            "value": "elfriedaroudebushloveschicken@yahoo.com"
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.put(url + "updateUser", data=json.dumps(payload), headers=headers)
        print(response.text)
        assert response.status_code == 200
        assert response.ok

        response = requests.get(url + "getUser?uuid=e820ce78-9499-41f2-84ef-1da35946240b", data=json.dumps(payload), headers=headers)
        result = response.json()
        print(result["Item"]["email"] == "elfriedaroudebushloveschicken@yahoo.com")

    def test_invalid_name_1(self):
        payload = {
            "uuid": "21843d4c-51bb-4d85-a066-75047d19086b",
            "key": "name",
            "value": 69
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.put(url + "updateUser", data=json.dumps(payload), headers=headers)
        print(response.content.decode())
        assert response.status_code == 400
        assert response.content.decode() == "Invalid Name"

    def test_invalid_name_2(self):
        payload = {
            "uuid": "21843d4c-51bb-4d85-a066-75047d19086b",
            "key": "name",
            "value": 420
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.put(url + "updateUser", data=json.dumps(payload), headers=headers)
        print(response.content.decode())
        assert response.status_code == 400
        assert response.content.decode() == "Invalid Name"

    def test_invalid_birthdate_1(self):
        payload = {
            "uuid": "ebdd8907-65b8-46e4-a714-f0c15ab450f2",
            "key": "birthdate",
            "value": "249199200.0"
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.put(url + "updateUser", data=json.dumps(payload), headers=headers)
        print(response.content.decode())
        assert response.status_code == 400
        assert response.content.decode() == "Invalid Birthdate"

    def test_invalid_birthdate_2(self):
        payload = {
            "uuid": "ebdd8907-65b8-46e4-a714-f0c15ab450f2",
            "key": "birthdate",
            "value": "Insert birthdate here"
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.put(url + "updateUser", data=json.dumps(payload), headers=headers)
        print(response.content.decode())
        assert response.status_code == 400
        assert response.content.decode() == "Invalid Birthdate"
    
    def test_invalid_sex_1(self):
        payload = {
            "uuid": "bef6c25e-a162-472d-ae7f-7b7ab6c42b31",
            "key": "sex",
            "value": "bi"
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.put(url + "updateUser", data=json.dumps(payload), headers=headers)
        print(response.content.decode())
        assert response.status_code == 400
        assert response.content.decode() == "Invalid Sex"

    def test_invalid_sex_2(self):
        payload = {
            "uuid": "bef6c25e-a162-472d-ae7f-7b7ab6c42b31",
            "key": "sex",
            "value": "demi"
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.put(url + "updateUser", data=json.dumps(payload), headers=headers)
        print(response.content.decode())
        assert response.status_code == 400
        assert response.content.decode() == "Invalid Sex"

    def test_invalid_email_1(self):
        payload = {
            "uuid": "e820ce78-9499-41f2-84ef-1da35946240b",
            "key": "email",
            "value": "Insert email here"
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.put(url + "updateUser", data=json.dumps(payload), headers=headers)
        print(response.content.decode())
        assert response.status_code == 400
        assert response.content.decode() == "Invalid Email"

    def test_invalid_email_2(self):
        payload = {
            "uuid": "e820ce78-9499-41f2-84ef-1da35946240b",
            "key": "email",
            "value": "Insert another email here"
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.put(url + "updateUser", data=json.dumps(payload), headers=headers)
        print(response.content.decode())
        assert response.status_code == 400
        assert response.content.decode() == "Invalid Email"

    def test_invalid_key_1(self):
        payload = {
            "uuid": "e820ce78-9499-41f2-84ef-1da35946240b",
            "key": "Hair Color",
            "value": "black"
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.put(url + "updateUser", data=json.dumps(payload), headers=headers)
        print(response.content.decode())
        assert response.status_code == 400
        assert response.content.decode() == "Invalid Key"

    def test_invalid_key_2(self):
        payload = {
            "uuid": "e820ce78-9499-41f2-84ef-1da35946240b",
            "key": "Favorite Word",
            "value": "supercalifragilisticexpialidocious"
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.put(url + "updateUser", data=json.dumps(payload), headers=headers)
        print(response.content.decode())
        assert response.status_code == 400
        assert response.content.decode() == "Invalid Key"

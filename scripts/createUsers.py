import requests
import sys
import uuid
import names
import random
import json

def createUsers(num, url):
    for i in range(num):
        if (random.randint(1, 2) % 2 == 0):
            sex = "female"
        else:
            sex = "male"
        payload = {    
            "uuid": str(uuid.uuid4()),
            "name": names.get_full_name(),
            "age": random.randint(18, 100),
            "sex": sex,
            "email": "someboody@inbox.email.message.eu.com"
        }
        # Content-Type:application/json
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url + "createUser", data=json.dumps(payload), headers=headers)
        print(response.text, response.status_code)

def main():
    if (len(sys.argv) > 1):
        try: 
            createUsers(int(sys.argv[1]), sys.argv[2])
        except:
            print("invalid input")
    else:
        print("Missing required parameters: number of users, url")

main()
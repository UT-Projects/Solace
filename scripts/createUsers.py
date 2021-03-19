import requests
import sys
import uuid
import names
import random

def createUsers(num, url):
    for i in range(num):
        if (random.randint(1, 2) % 2 == 0):
            sex = "female"
        else:
            sex = "male"
        data = {    
            "UUID": str(uuid.uuid4()),
            "Name": names.get_full_name(),
            "Age": random.randint(18, 100),
            "Sex": sex,
            "Email": "someboody@inbox.email.message.eu.com"
        }
        response = requests.post(url, data=data)
        print(response)

def main():
    if (len(sys.argv) > 1):
        createUsers(sys.argv[1], sys.argv[2] + ":" + sys.argv[3])
    else:
        print("Missing required parameters: number of users, url, port")

main()
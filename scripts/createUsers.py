import requests
import sys
import uuid
import names
import random
import json
import datetime
import calendar

def createUsers(num, url):
    for i in range(num):
        if (random.randint(1, 2) % 2 == 0):
            sex = "female"
        else:
            sex = "male"
        payload = {    
            "uuid": str(uuid.uuid4()),
            "name": names.get_full_name(),
            "birthdate": random_birthdate(),
            "sex": sex,
            "email": "someboody@inbox.email.message.eu.com"
        }
        # Content-Type:application/json
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url + "createUser", data=json.dumps(payload), headers=headers)
        print(response.text, response.status_code)

def random_birthdate():
    earliest = datetime.date(1910,1,1)
    latest  = datetime.date(2018,1,1)
    delta = latest - earliest
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds    
    random_second = random.randrange(int_delta)
    date = earliest + datetime.timedelta(seconds = random_second)
    return calendar.timegm(date.timetuple())

def random_date():
    randomYear = random.randrange(1920, 2010)
    randomMonth = random.randrange(1, 13)
    
    if randomMonth == 2:
        maxDay = 28 if not isLeapYear(randomYear) else 29
    elif randomMonth in [4, 6, 9, 11]:
        maxDay = 30
    else:
        maxDay = 31

    randomDay = random.randrange(1, maxDay + 1)

    return datetime.datetime(randomYear, randomMonth, randomDay).timestamp()

def isLeapYear(year):
    return year % 4 == 0

def main():
    if (len(sys.argv) > 1):
        try: 
            createUsers(int(sys.argv[1]), sys.argv[2])
        except Exception as e:
            print(e)
    else:
        print("Missing required parameters: number of users, url")

main()
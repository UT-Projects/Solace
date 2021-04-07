import pytest
import os
import time
import requests
import boto3
from dotenv import load_dotenv

load_dotenv()

def createsession():
    try:
        session = boto3.session.Session(aws_access_key_id="anything", aws_secret_access_key="anything", region_name="us-east-1")
        dynamodb = session.resource('dynamodb', endpoint_url='http://localhost:8000/')
    except Exception as e:
        print('Could not create dynamodb session.')

        assert False

    return dynamodb

def createuserdatatable(dynamodb):
    try:
        table = dynamodb.create_table(TableName="user_profile",KeySchema=[{ 'AttributeName': "uuid", 'KeyType': "HASH" }],AttributeDefinitions=[{ 'AttributeName': "uuid", 'AttributeType': "S" }],ProvisionedThroughput={'ReadCapacityUnits': 1,'WriteCapacityUnits': 1} )
        
        return table.table_status
    except Exception as e:
        return "Did not create: " + str(e)

def createusers(dynamodb, table):
    try:
        table = dynamodb.Table(table)
        users = [
            # delete user
            ('2d99ce89-d882-4578-a75c-024c099b1d24', 'Nicole Carvajal', 1030942800, 'male', 'nicolecarvajal@gmail.com'),
            ('1e0dc55a-1de1-4349-86a3-089da3cde919', 'Joseph Zenger', 294642000, 'male', 'josephZ@inbox.email.message.eu.com'),
            ('7cb19016-1343-4226-8b59-89dd079be6e6', 'Lura Abdi', 214808400, 'female', 'luraabdi125@yahoo.com'),
            ('8be74c06-9657-44c6-9ede-4424a698e3e3', 'Lisa Brown', 486104400, 'male', 'LisaBrown@hotmail.com'),
            # update user
            ('21843d4c-51bb-4d85-a066-75047d19086b', 'Steven Bak', 892789200, 'female', 'stevenb@gmail.com'),
            ('ebdd8907-65b8-46e4-a714-f0c15ab450f2', 'Reginald Hughes', 249199200, 'male', 'bigdogregi@gmail.com'),
            ('bef6c25e-a162-472d-ae7f-7b7ab6c42b31', 'Warren Alexander', 1053838800, 'female', 'waralex23@yahoo.com'),
            ('e820ce78-9499-41f2-84ef-1da35946240b', 'Elfrieda Roudebush', 620802000, 'male', 'elfriedaroudebushloveschicken@yahoo.com'),
            # get user
            ('510d2b66-b86a-4271-b175-c127e6c19e53', 'Samuel Menist', 1128834000, 'female', 'sami@gmail.com'),
            ('76969fee-b50c-49fc-8b65-3a8770bc05ec', 'Brian Chugg', 354949200, 'female', 'brianisabigboy14@yahoo.com'),
        ]

        for user in users:
            table.put_item(
                Item={
                    "uuid": user[0],
                    "name": user[1],
                    "birthdate": user[2],
                    "sex": user[3],
                    "email": user[4]
                }
            )

        return "Created users."
    except Exception as e:
        return "Could not create users: " + str(e)


def healthcheck():
    max_tries = 50
    headers = {'Content-Type': 'application/json'}

    for i in range(max_tries):
        response = requests.get('http://localhost:3000/healthcheck', headers=headers)
        status = response.status_code
        if (status == 200):
            break
        time.sleep(0.1)
        
    print(response.text, response.status_code)

    if(status and status == 200):
        return True
    
    return False

@pytest.fixture(scope="session", autouse=True)
def execute_before_any_test():
    print("Fixture")
    assert healthcheck()
    # os.system("node scripts/createTable.js")
    session = createsession()

    print("createTable: ", createuserdatatable(session))
    print("createUsers: ", createusers(session, "user_profile"))

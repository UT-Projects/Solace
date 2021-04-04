import pytest
import os
import time
import requests
import boto3
from dotenv import load_dotenv

load_dotenv()

def createuserdatatable():
    try:
        dynamodb = boto3.session('dynamodb', aws_access_key="anything", aws_secret_access_key="anything", region_name="us-east-1", endpoint_url="http://localhost:8000/")
        table = dynamodb.create_table(TableName="user_profile",KeySchema=[{ 'AttributeName': "uuid", 'KeyType': "HASH" }],AttributeDefinitions=[{ 'AttributeName': "uuid", 'AttributeType': "S" }],ProvisionedThroughput={'ReadCapacityUnits': 1,'WriteCapacityUnits': 1} )
        return table.table_status
    except Exception as e:
        return "Did not create: " + str(e)

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
    print("createTable: ", createuserdatatable())

require('dotenv').config()
const AWS = require('aws-sdk')
const { DynamoDB } = require('aws-sdk')

AWS.config.update({
    endpoint: process.env.AWS_ENDPOINT || "dynamodb.us-east-1.amazonaws.com",
    region: process.env.AWS_DEFAULT_REGION || "us-east-1",
    accessKeyId: process.env.AWS_ACCESS_KEY_ID,
    secretAccessKey: process.env.AWS_SECRET_ACCESS_KEY,
});

const docClient = new AWS.DynamoDB.DocumentClient();

const getDocument = (tableName, uuid) => {
    var params = {
        TableName: tableName,
        Key: {
            "UUID": uuid,
        },
    };
    
    return new Promise(function(resolve, reject) {
        docClient.get(params, function(error, data) {
            if (error) {
                reject(JSON.stringify(error, null, 2));
            } else {
                resolve(JSON.stringify(data, null, 2));
            }
        });
    })
}

const updateDocument = (tableName, uuid, key, value) => {
    var params = {
        TableName: tableName,
        Key: {
            "UUID": uuid,
        },
        UpdateExpression: "set #name = :n",
        ExpressionAttributeNames: { // use because key might be reserved word in DynamoDB
            "#name" : key,
        },
        ExpressionAttributeValues: {
            ":n" : value,
        },
        ReturnValues: "UPDATED_NEW", // return only updated values
    };
    
    return new Promise(function(resolve, reject) {
        docClient.update(params, function(error, data) {
            if (error) {
                reject(JSON.stringify(error, null, 2));
            } else {
                resolve(JSON.stringify(data, null, 2));
            }
        });
    })
}

const createDocument = (tableName, partitionKey, sortKey, item) => {
    var params = {
        TableName: tableName,
        Item: item,
        ConditionExpression: "{partitionKey} <> :yearKeyVal AND #title <>  :title",
        ReturnValues: "NONE | ALL_OLD | UPDATED_OLD | ALL_NEW | UPDATED_NEW",
    };

    return new Promise(function(resolve, reject) {
        docClient.put(params, function(error, data) {
            if (error) {
                reject(JSON.stringify(error, null, 2));
            } else {
                resolve(JSON.stringify(data, null, 2));
            }
        })
    });
}

const deleteDocument = (tableName, primaryKey) => {
    var params = {
        TableName: tableName,
        Key: primaryKey,
    };

    return new Promise(function(resolve, reject) {
        docClient.delete(params, function(err, data) {
            if (error) {
                reject(JSON.stringify(error, null, 2));
            } else {
                resolve(JSON.stringify(data, null, 2));
            }
        })
    });
}

module.exports = {
    getDocument,
    updateDocument,
    createDocument,
    deleteDocument,
    docClient
}

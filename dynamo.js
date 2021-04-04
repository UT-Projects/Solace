require('dotenv').config()
const AWS = require('aws-sdk')

AWS.config.update({
    endpoint: process.env.AWS_ENDPOINT || "http://localhost:8000",
    region: process.env.AWS_DEFAULT_REGION || "us-east-1",
    accessKeyId: process.env.AWS_ACCESS_KEY_ID || "anything",
    secretAccessKey: process.env.AWS_SECRET_ACCESS_KEY || "anything",
});

const docClient = new AWS.DynamoDB.DocumentClient();

const getDocument = (tableName, uuid) => {
    var params = {
        TableName: tableName,
        Key: {
            "uuid": uuid,
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
            "uuid": uuid,
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

const createDocument = (tableName, item) => {
    var params = {
        TableName: tableName,
        Item: item,
        ConditionExpression: "attribute_not_exists(#uuid)",
        ExpressionAttributeNames: {
            "#uuid": "uuid",
        },
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
        docClient.delete(params, function(error, data) {
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

require('dotenv').config()
const AWS = require('aws-sdk')
const { DynamoDB } = require('aws-sdk')

AWS.config.update({
  endpoint: process.env.AWS_ENDPOINT,
  region: process.env.AWS_DEFAULT_REGION,
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

const getUser = (uuid) => {
  return getDocument("user_profile", uuid);
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
    ReturnValues:"UPDATED_NEW", // return only updated values
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

const updateUser = (uuid, key, value) => {
  return updateDocument("user_profile", uuid, key, value);
}

module.exports = {
  getDocument,
  getUser,
  updateDocument,
  updateUser,
}

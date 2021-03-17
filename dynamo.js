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

module.exports = {
  getDocument,
  getUser,
}

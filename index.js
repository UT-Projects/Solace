const express = require('express')
const AWS = require('aws-sdk')
const app = express()
const server = express()
const port = 3000
const base_url = '/'

AWS.config.update({
    endpoint: 'dynamodb.us-east-1.amazonaws.com'
});

const docClient = new AWS.DynamoDB.DocumentClient();

app.use(express.json())
app.use(function (req, res, next) {
    res.setHeader('Access-Control-Allow-Origin', '*');
    // res.setHeader('Access-Control-Allow-Methods', 'GET,POST,DELETE');
    res.setHeader('Access-Control-Allow-Headers', 'Content-Type, Access-Control-Allow-Headers');
    next();
  });

app.get('/healthcheck', (req, res) => {
    res.status(200).send("Connection Success");
})


server.use(base_url, app)
server.listen(port, () => {
  console.log(`App running at base url ${base_url} with port ${port}.`)
})




// amazon uses environment variables AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY and AWS_REGION
// these can be found by going to portal, clicking name at top right, selecting my security credentials, region is us-east-1
// make sure and restart terminal after setting variables

// params for GetItem
var params = {
  TableName: "user_profile",
  Key: {
    "UUID": "24086hqw03r8ejta0dut0a",
  },
};

// get item in user_profile table with UUID 24086hqw03r8ejta0dut0a
docClient.get(params, function(err, data) {
  if (err) {
      console.error("Unable to read item. Error JSON:", JSON.stringify(err, null, 2));
  } else {
      console.log("GetItem succeeded.", JSON.stringify(data, null, 2));
  }
});

// params for UpdateItem
var params = {
  TableName: "user_profile",
  Key: {
    "UUID": "24086hqw03r8ejta0dut0a",
  },
  UpdateExpression: "set #name = :n",
  ExpressionAttributeNames: { // use because Name is reserved word in DynamoDB
    "#name" : "Name",
  },
  ExpressionAttributeValues: {
    ":n" : "Anshul Modh",
  },
  ReturnValues:"UPDATED_NEW", // return only updated values
};

// update item in user_profile table with UUID 24086hqw03r8ejta0dut0a
// change Name Anshul Mode -> Anshul Modh
docClient.update(params, function(err, data) {
  if (err) {
      console.error("Unable to update item. Error JSON:", JSON.stringify(err, null, 2));
  } else {
      console.log("UpdateItem succeeded.", JSON.stringify(data, null, 2));
  }
});
require('dotenv').config()
const express = require('express')
const app = express()
const server = express()
const port = process.env.API_PORT || 3000
const base_url = process.env.BASE_URL || '/'

const dynamo = require('./dynamo')

app.use(express.json())
app.use(function (req, res, next) {
    res.setHeader('Access-Control-Allow-Origin', '*');
    // res.setHeader('Access-Control-Allow-Methods', 'GET,POST,DELETE');
    res.setHeader('Access-Control-Allow-Headers', 'Content-Type, Access-Control-Allow-Headers');
    next();
  });

const noErrorHandle = (res, future) => {
  future
  .then(response => res.status(200).send(response))
  .catch(error => res.status(500).send(error))
}

app.get('/healthcheck', (req, res) => {
  res.status(200).send("Connection Success");
})

app.get('/getUser', (req, res) => {
  noErrorHandle(res, dynamo.getUser(req.query.uuid))
});

app.get('/getDocument', (req, res) => {
  noErrorHandle(res, dynamo.getDocument(req.query.tableName, req.query.uuid))
});

app.post('/updateDocument', (req, res) => {
  noErrorHandle(res, dynamo.updateDocument(req.body.tableName, req.body.uuid, req.body.key, req.body.value))
});

app.post('/updateUser', (req, res) => {
  noErrorHandle(res, dynamo.updateUser(req.body.uuid, req.body.key, req.body.value))
});

server.use(base_url, app)
server.listen(port, () => {
  console.log(`App running at base url ${base_url} with port ${port}.`)
})
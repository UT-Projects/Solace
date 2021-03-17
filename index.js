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

app.get('/healthcheck', (req, res) => {
    res.status(200).send("Connection Success");
})

server.use(base_url, app)
server.listen(port, () => {
  console.log(`App running at base url ${base_url} with port ${port}.`)
})

app.get('/getUser', (req, res) => {
  dynamo.getUser(req.query.uuid)
  .then(response => res.status(200).send(response))
  .catch(error => res.status(500).send(error))
});

app.get('/getDocument', (req, res) => {
  dynamo.getDocument(req.query.tableName, req.query.uuid)
  .then(response => res.status(200).send(response))
  .catch(error => res.status(500).send(error))
});
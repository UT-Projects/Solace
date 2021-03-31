require('dotenv').config()
const express = require('express')
const app = express()
const server = express()
const port = process.env.API_PORT || 3000
const base_url = process.env.BASE_URL || '/'

const dynamo = require('./dynamo')
const user = require('./user')
const validate = require('./validate')

app.use(express.json());
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
});

app.get('/getUser', (req, res) => {
    noErrorHandle(res, user.getUser(req.query.uuid))
});

// app.get('/getDocument', (req, res) => {
//     noErrorHandle(res, dynamo.getDocument(req.query.tableName, req.query.uuid))
// });

// app.post('/updateDocument', (req, res) => {
//     noErrorHandle(res, dynamo.updateDocument(req.body.tableName, req.body.uuid, req.body.key, req.body.value))
// });

app.put('/updateUser', (req, res) => {
    noErrorHandle(res, user.updateUser(req.body.uuid, req.body.key, req.body.value))
});

app.post('/createUser', (req, res) => {
    [uuid, n, age, sex, email] = [req.body.uuid, req.body.name, req.body.age, req.body.sex.toLowerCase(), req.body.email];
    //Error check age

    if(!Number.isInteger(age)) {
        res.status(400).send("Invalid age");
    }
    
    //Error check sex
    else if(sex !== 'male' && sex !== 'female') {
        res.status(400).send("Invalid sex");
    }

    //Error check uuid
    else if(!validate.validateUUIDFormat(uuid)) {
        res.status(400).send("Invalid UUID Format");
    }
    else {
        noErrorHandle(res, user.createUser(uuid, n, age, sex, email))
    }
});

app.delete('/deleteUser', (req, res) => {
    noErrorHandle(res, user.deleteUser(req.query.uuid))
});

server.use(base_url, app);
server.listen(port, () => {
  console.log(`App running at base url ${base_url} with port ${port}.`)
});
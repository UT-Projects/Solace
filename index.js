require('dotenv').config()
const express = require('express')
const app = express()
const server = express()
const handling = express()
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

    switch (req.body.key) {
        case "uuid":
            if(!validate.validateUUIDFormat(req.body.value)) {
                res.status(400).send("Invalid UUID");
                return;
            }
            break;
        case "name":
            if(req.body.value === "" || typeof req.body.value != "string") {
                res.status(400).send("Invalid Name");
                return;
            }
            break;
        case "birthdate":
            if(!Number.isFinite(req.body.value)) {
                res.status(400).send("Invalid Birthdate");
                return;
            }
            break;
        case "sex":
            if(typeof req.body.value != "string" || (req.body.value.toLowerCase() != "male" && req.body.value.toLowerCase() != "female")) {
                res.status(400).send("Invalid Sex");
                return;
            }
            req.body.value = req.body.value.toLowerCase();
            break;
        case "email":
            if (!validate.validateEmail(req.body.value)) {
                res.status(400).send("Invalid Email");
                return;
            }
            break;
        default:
            res.status(400).send("Invalid Key");
            return;
    }

    noErrorHandle(res, user.updateUser(req.body.uuid, req.body.key, req.body.value))
});

app.post('/createUser', (req, res) => {
    [uuid, n, birthdate, sex, email] = [req.body.uuid, req.body.name, req.body.birthdate, req.body.sex, req.body.email];

    if(!validate.validateUUIDFormat(uuid))
        res.status(400).send("Invalid UUID");

    else if(n === "" || typeof n != "string")
        res.status(400).send("Invalid Name");

    else if(!Number.isFinite(birthdate))
        res.status(400).send("Invalid Birthdate");

    else if(typeof sex != "string" || (sex.toLowerCase() != "male" && sex.toLowerCase() != "female"))
        res.status(400).send("Invalid Sex");

    else if (!validate.validateEmail(email))
        res.status(400).send("Invalid Email");

    else
        noErrorHandle(res, user.createUser(uuid, n, birthdate, sex.toLowerCase(), email));
        
});

app.delete('/deleteUser', (req, res) => {
    noErrorHandle(res, user.deleteUser(req.query.uuid))
});

server.use(base_url, app);
server.listen(port, () => {
  console.log(`App running at base url ${base_url} with port ${port}.`)
});

var http = require("http");
const execution = http.createServer(handling);
execution.listen(3001, () => {
    console.log('HTTP server listening on port 3001');
});

const io = require('socket.io')(execution);
io.on('connection', (socketServer) => {
  socketServer.on('npmStop', () => {
    process.exit(0);
  });
});

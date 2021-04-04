const { LexModelBuildingService } = require('aws-sdk');
const { v4: uuidv4 } = require('uuid');
const dynamo = require('./dynamo')

const getUser = (uuid) => {
    return dynamo.getDocument("user_profile", uuid);
}

const updateUser = (uuid, key, value) => {
    return dynamo.updateDocument("user_profile", uuid, key, value);
}

const createUser = (uuid, name, birthdate, sex, email) => {
    item = {
        "uuid": uuid,
        "name": name,
        "birthdate": birthdate,
        "sex": sex,
        "email": email
    }
    return dynamo.createDocument("user_profile", item);
}

const deleteUser = (uuid) => {
    primaryKey = {
        "uuid": uuid
    }
    return dynamo.deleteDocument("user_profile", primaryKey);
}

module.exports = {
    getUser,
    updateUser,
    createUser,
    deleteUser,
}
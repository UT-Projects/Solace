const { LexModelBuildingService } = require('aws-sdk');
const { v4: uuidv4 } = require('uuid');
const dynamo = require('./dynamo')

const getUser = (uuid) => {
    return dynamo.getDocument("user_profile", uuid);
}

const updateUser = (uuid, key, value) => {
    return dynamo.updateDocument("user_profile", uuid, key, value);
}

const createUser = (uuid, name, age, sex, email) => {
    item = {
        "UUID": uuid,
        "Name": name,
        "Age": age,
        "Sex": sex,
        "Email": email
    }
    return dynamo.createDocument("user_profile", item);
}

const deleteUser = (uuid) => {
    primaryKey = {
        "UUID": uuid
    }
    return dynamo.deleteDocument("user_profile", primaryKey);
}

module.exports = {
    getUser,
    updateUser,
    createUser,
    deleteUser,
}
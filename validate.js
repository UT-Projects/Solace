// const validateEmail = (email) => {
//     // check for @ sign
//     var atSymbol = email.indexOf("@");
//     if(atSymbol < 1) return false;
    
//     var dot = email.indexOf(".");
//     if(dot <= atSymbol + 2) return false;
    
//     // check that the dot is not at the end
//     if (dot === email.length - 1) return false;
    
//     return true;
// }

const validateEmail = (email) => {
    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
}

const validateUUIDFormat = (uuid) => {
    return /^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/.test(uuid);
}

module.exports = {
    validateEmail,
    validateUUIDFormat,
}
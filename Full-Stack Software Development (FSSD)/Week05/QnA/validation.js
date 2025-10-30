// function add(a,b) {    
//     try {
//         a = castToNumber(a);
//         b = castToNumber(b);
//     } catch(error) {
//         console.log("error")
//         return NaN
//     }

//     return a + b;
// }

// function castToNumber(value) {
//     if (Number.isNaN(Number(value)))
//         throw new Error("Value can not be converted to a number")
    
//     return Number(value);
// }

// console.log(add("", "1"))

class User {
    constructor(username, password, email) {
        this.username = username;
        this.password = password;
        this.email = email;
    }
}

const userDB = [];

function createNewUser(username, password, email){
    if (username === undefined || username === null){
        throw new Error("Username is required")
    }

    if (password === undefined || password === null){
        throw new Error("Password is required")
    }

    const regex = /^.{8,}$/
    if (regex.test(password)){
        throw new Error("Passowrd must have 8 or more characters")
    }

    const newUser = new User(username, password, email);

    userDB.push(newUser);
}

createNewUser("bongani", "12345678", "bongani@emai.com")
createNewUser("raul", "raul123", "raul@email.com")
createNewUser("jack", "raul@email.com");

console.log(userDB)
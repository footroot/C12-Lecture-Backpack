// fetch('https://jsonplaceholder.typicode.com/todos/1')
//     .then(response => response.json())
//     .then((json) => console.log(json))

// // synchronous
// console.log("Start");
// for (let i = 1; i < 10; i++){
//     console.log(i);
// }
// console.log("End");


// console.log("*************");

// // asynchronous
// console.log("Start");
// setTimeout(() => console.log("Middle"), 1000);
// console.log("End");


// promise chaining
fetch('https://jsonplaceholder.typicode.com/todos/1')
    .then(response => response.json())
    .then(post => {
        console.log(post);
        return fetch("https://jsonplaceholder.typicode.com/users/1")
    })
    .then(response => response.json())
    .then(user => console.log(user))
    .catch(error => console.error("Error: ", error));


    // async/await
async function fetchUser() {
    try {
        const response = await fetch("https://jsonplaceholder.typicode.com/users/1");
        const user = await response.json();
        console.log(user);
    } catch (error) {
        console.error('Error: ', error);
    }
}

fetchUser();
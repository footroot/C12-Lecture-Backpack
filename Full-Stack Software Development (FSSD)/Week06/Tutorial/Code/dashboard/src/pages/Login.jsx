import { useNavigate } from "react-router-dom";

export default function Login({setUserDetails}) {    
    const navigate = useNavigate();

    const handleLogin = (e) => {
        e.preventDefault();
        const username = e.target.username.value;
        const password = e.target.password.value;

        if (! (username || password)) {
            alert("Please enter username and password");
            e.target.username.focus();
            return;
        }

        const user = validateUser(username);

        if (!user) {
            alert("Invalid username or password");
            e.target.username.focus();
            return;
        }

        setUserDetails(user);
        navigate("/dashboard");
    }

    return (
        <>
            <h1>Login Page</h1>

            <form onSubmit={handleLogin}>
                <label for="username">Username:</label>
                <input type="text" id="username" name="username" />
                <br />
                <label for="password">Password:</label>
                <input type="password" id="password" name="password" />
                <br />
                <button type="submit">Login</button>
            </form>
        </>
    )
}

// FAKE API
function validateUser(username) {
    const userDetails = {
        "jimmy": {
            "username": "jimmy",
            "age": 25,
            "favoriteColor": "blue",
            "isAdmin": false,
            "jobTitle": "Programmer",
            "email": "jimmy@example.com"
        },
        "bob": {
            "username": "bob",
            "age": 30,
            "favoriteColor": "red",
            "isAdmin": true,
            "jobTitle": "Manager",
            "email": "bob@example.com"
        },
        "alice": {
            "username": "alice",
            "age": 22,
            "favoriteColor": "green",
            "isAdmin": false,
            "jobTitle": "Designer",
            "email": "alice@example.com"
        },
        "john": {
            "username": "john",
            "age": 35,
            "favoriteColor": "yellow",
            "isAdmin": true,
            "jobTitle": "Developer",
            "email": "john@example.com"
        }
    }

    return userDetails[username];
}
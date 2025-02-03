import express from "express";
import jwt from "jsonwebtoken";
import cors from "cors"

const app = express();

app.use(express.json());
app.use(cors())
app.listen(8080, () => {
  console.log("Server is running on http://localhost:8080");
});

app.post("/login", (req, res) => {
  const { username, password } = req.body;

  if (username === "John" && password === "1234") {
    const payload = {
      username: username,
      admin: false,
    };

    const token = jwt.sign(JSON.stringify(payload), "secret", {
      algorithm: "HS256",
    });

    res.json({
      message: "Login was successful",
      token: token,
    });
  } else {
    res.status(400).json({ error: "Username or password invalid!" });
  }
});

app.get("/resource", (req, res) => {
  const authHeaders = req.headers["authorization"];
  const token = authHeaders.split(" ")[1];


    try {
        const decode = jwt.verify(token, "secret");

        res.json({ message: `Your token has been verified: ${decode.username}` });

    } catch (error) {
        res.status(401).json({error: error})

    }

});

app.get('/admin_resource', (req, res)=>{
    const authHeaders = req.headers['authorization']
    const token = authHeaders.split(' ')[1]


    try {
        const decoded = jwt.verify(token, 'dog')

        console.log(decoded)
        if (decoded.admin) {
            res.json({
                message: 'Access granted!!'
            })
        } else {
            res.status(403).json({
                'error': 'You JWT was verified, but you do not have admin access.'
            })
        }
    } catch (error) {
        res.json(error)
    }

})
import express from "express";
import cors from "cors"

function auth(req, res, next) {
    const {api_key} = req.query;

    if (!api_key){
        res.status(401).json({
            message: "Missing API KEY"
        })
    }

    if (api_key != "secretkey"){
        res.status(401).json({
            message: "Invalid API key"
        })
    }    

    next();
}

const app = express();
app.use(express.json())
app.use(cors())
app.use(auth)

function getBooks(req, res) {
    const {author} = req.query;

    res.status(200).json({
        author: author,
        title: "Random title"
    })
}

app.get("/", getBooks)
app.get("/book", (req, res) => {
    const value = req.bonganis_value
    res.send({
        title: "This has no auth",
        value
    })
})


app.listen(8080, () => console.log("listening on: http://localhost:8080"))
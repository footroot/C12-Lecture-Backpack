import express from "express"
import mongoose from "mongoose";
import router from "./routes/index.js";

const app = express()

app.use(express.json())

const uri = "mongodb+srv://danw:nnt2LNYkPqPefGz8@cluster0.wkxjt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0";

const clientOptions = { serverApi: { version: '1', strict: true, deprecationErrors: true } };

// MVC

mongoose.connect(uri, clientOptions)
.then(()=>{
    console.log('Connection to mongodb done successfully...')
})
.catch((error)=>{
    console.log(error)
})


app.use('/', router)

app.listen(8080, ()=>{
    console.log('Server is running on http://localhost:8080')
})
// Imports
import express from "express"
import mongoose from "mongoose"
import { routes } from "./routes/index.js";
import cors from "cors"

// Initialize express
const app = express()

app.use(express.json())
app.use(cors())

// Initialize Mongoose (MongoDB)
const uri = `mongodb+srv://danw:SkDkYViaijyBVzT3@cluster0.q3mev.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0`;
const clientOptions = { serverApi: { version: '1', strict: true, deprecationErrors: true } };

mongoose.connect(uri, clientOptions)
.then(()=>{
    console.log('Connected to MongoDB')
}).catch((error)=>{
    console.log(error)
})

// Listen to PORT 8080
// const PORT = process.env.PORT
app.listen(8080, ()=>{
    console.log('Server is running on http://localhost:8080')
})

// Initialize routes
app.use('/', routes)

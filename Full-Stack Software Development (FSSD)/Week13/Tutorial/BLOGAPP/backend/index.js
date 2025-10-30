import express from "express"
import { routes } from "./routes/index.js"
import cors from "cors"
const app = express()

app.use(cors())
app.use('/', routes)


app.listen(8070, ()=>{
    console.log('http://localhost:8070')
})
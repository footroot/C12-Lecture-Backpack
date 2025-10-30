import express from 'express'
import { routes } from './routes/index.js'

const app = express()
app.use(express.json())
// Middlewares
app.listen(8080, ()=>{
    console.log('Server is starting on http://localhost:8080')
})

app.use(routes)
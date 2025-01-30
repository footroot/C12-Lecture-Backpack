import express from "express"
import { helloWorld, createBook, getBooks  } from "../controllers/index.js"

const routes = express.Router()

routes.get('/', helloWorld)
routes.post('/create-book', createBook)
routes.get('/books', getBooks)

export {
    routes
}
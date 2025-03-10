import express from "express"
import { getHomePage, getBlogs } from "../controllers/index.js"

const routes = express.Router()

routes.get('/', getHomePage)
routes.get('/blogs', getBlogs)

export {
    routes
}
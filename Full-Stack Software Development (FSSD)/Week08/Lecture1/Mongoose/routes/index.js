import express from "express"
import { getBlogs, createBlog } from "../controllers/index.js"
const router = express.Router()

router.get('/blogs', getBlogs)
router.post('/blogs', createBlog)

export default router
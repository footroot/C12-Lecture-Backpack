// Act as our views
import express from "express"
import { helloWorld, createBlog, getBlogs, updateBlog, deleteBlog } from "../controllers/index.js"

const router = express.Router()

router.get('/', helloWorld)
router.post('/create-blog', createBlog)
router.get('/blogs', getBlogs)
router.put('/blog-update/:id', updateBlog)
router.delete('/blog-delete/:id', deleteBlog)
export default router
import mongoose from "mongoose"

const blogSchema = mongoose.Schema({
    title: String,
    content: String,
    author: String
})

const BlogModel = mongoose.model('Blog', blogSchema)

export default BlogModel
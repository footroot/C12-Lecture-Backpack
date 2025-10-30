import BlogModel from "../models/index.js"

const getBlogs = async (req, res)=>{
    const blogs = await BlogModel.find()

    res.json(blogs)
}

const createBlog = async (req, res)=>{
    const { title, content, author } = req.body
    const blog = await BlogModel.create({
        title: title,
        content: content,
        author: author
    })

    const savedBlog = await blog.save()
    res.json({
        message: 'Blog saved successfully',
        savedBlog: savedBlog
    })

}


export {
    getBlogs,
    createBlog
}
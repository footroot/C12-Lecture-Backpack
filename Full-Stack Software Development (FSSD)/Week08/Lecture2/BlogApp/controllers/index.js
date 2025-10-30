import { blogModel } from "../models/index.js"
// Busines  logic of application
const helloWorld = (req, res)=>{
    res.send('Hello World')
}

// CRUD
// Create
const createBlog = async (req, res)=>{
    const { title, content, author } = req.body

    if (!title || !content || !author) {
        res.status(400).json({message: 'Please insert valid details'})
    }
    
    const blog = await blogModel.create({
        title,
        content,
        author
    })
    const savedBlog = await blog.save()

    res.json({message: 'Blog created successfully.'})
}

// Read
const getBlogs = async (req, res)=>{
    const blogs = await blogModel.find()
    res.json(blogs)
}

// Update
const updateBlog = async (req, res)=>{
    const { id } = req.params
    const { title, content, author } = req.body

    const blog = await blogModel.findByIdAndUpdate(id, {title, content, author}, {new: true})
    res.json({
        message: "Blog updated"
    })

}


// Delete
const deleteBlog = async (req, res)=>{
    const { id } = req.params

    const blog = await blogModel.findByIdAndDelete(id)
    res.json({
        message: 'Blog deleted successfully.'
    })
}
export {
    helloWorld,
    createBlog,
    getBlogs,
    updateBlog,
    deleteBlog
}
// Schema
import mongoose from "mongoose";

const blogSchema = mongoose.Schema({
    title: {
        required: true,
        type: String
    },

    content: {
        required: true,
        type: String
    },

    author: {
        required: true,
        type: String
    },

    createdAt: {
        type: Date,
        required: true,
        default: Date.now()
    }
})

const blogModel = mongoose.model('Blogs', blogSchema)

export {
    blogModel
}
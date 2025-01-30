import mongoose from "mongoose"

// Create a schema (define your document)
const bookSchema = mongoose.Schema({
    title: {
        type: String,
        required: true
    },
    author: {
        type: String,
        required: true
    },
    image: {
        type: String,
        required: true
    },
    genre: {
        type: String,
        required: true
    }

})

const BookModel = mongoose.model('Book', bookSchema)

export default BookModel
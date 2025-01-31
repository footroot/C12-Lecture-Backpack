import BookModel from "../models/index.js"

const helloWorld = (req, res)=>{
    res.json({message: 'Hello World'})
}

// CRUD Functionalities
// Create (Perform some error handling)
const createBook = async (req, res)=>{
    const { title, author, image, genre } = req.body

    console.log(title, author, image, genre)
    
    if ( !title || !author || !image || !genre ) {
        res.status(400).json({
            message: 'Invalid details'
        })
    }

    const book = await BookModel.create({
        title,
        author,
        image,
        genre: genre
    })

    const response = await book.save()

    res.status(200).json({
        message: 'Book saved successfully'
    })

}

// Read
const getBooks = async (req, res)=>{
    const books = await BookModel.find()
    res.status(200).json(books)
}

// Update
const updateBooks = (req, res)=>{

}

//Delete
const deleteBooks = (req, res)=>{

}


export {
    helloWorld,
    createBook,
    getBooks
}
import express from "express";
import cors from "cors";

const app = express();
app.use(express.json())
app.use(cors());

// Dummy Database
const books = [
    {
        id: 1,
        title: "The Great Gatsby",
        author: "F. Scott Fitzgerald",
        year: 1925,
        genre: "Fiction",
    },
    {
        id: 2,
        title: "The Catcher in the Rye",
        author: "J.D. Salinger",
        year: 1951,
        genre: "Fiction",
    },
    {
        id: 3,
        title: "To Kill a Mockingbird",
        author: "Harper Lee",
        year: 1960,
        genre: "Fiction",
    },
    {
        id: 4,
        title: "Pride and Prejudice",
        author: "Jane Austen",
        year: 1813,
        genre: "Fiction",
    }
]

app.use(express.static("public"))

app.get("/book/", (req, res) => {

    const { title } = req.query;

    const output = books.filter((book) => true)

    res.send(output);
});

app.get("/book/:id", (req, res) => {
    const { id } = req.params;

    const book = books.find((book) => book.id == id);
    console.log(book)

    if (!book)
        res.status(404).json({
            message: `Book with id ${id} does not exist`
        })

    res.status(200).json(book)
});

app.post("/book", (req, res) => {
    const { title, year, author, genre } = req.body;
    if (!title || !year || !author || !genre) {
        res.status(400).json({
            message: "All fields are required"
        })
    }

    const id = books.length + 1;
    books.push({
        id,
        title,
        year, 
        author,
        genre
    });

    res.status(203).json(
        books.at(-1)
    )
});

app.put("/book/:id", (req, res) => {
    const { title, year, author, genre } = req.body;
    if (!title || !year || !author || !genre) {
        res.status(400).json({
            message: "All fields are required"
        })
    }

    books.map((book) => {
        if (book.id == req.params.id){
            book = req.body
            book.id = req.params.id;
        }

        return book;
    })

    res.status(200);    
})

app.delete("/book/:id", (req, res) => {
    const output = books.filter((book) => book.id != req.params.id)
    res.status(200);
})

app.listen(8080, () => console.log("Server is running on port 8080"));
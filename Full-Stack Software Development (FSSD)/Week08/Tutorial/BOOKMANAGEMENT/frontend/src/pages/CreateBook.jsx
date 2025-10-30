import { useState } from "react";

const CreateBook = () => {
  const [title, setTitle] = useState("");
  const [author, setAuthor] = useState("");
  const [genre, setGenre] = useState("");
  const [image, setImage] = useState("");

  const submitData = async (bookTitle, bookAuthor, bookGenre, bookImage)=>{
    const bodyItem = {
        title: bookTitle,
        author: bookAuthor, 
        genre: bookGenre,
        image: bookImage
    }
    const response = await fetch('http://localhost:8080/create-book', {
        method: "POST",
        headers: {
            'Content-Type' : 'application/json'
        },
        body: JSON.stringify(bodyItem)
    })

    const data = await response.json()

    console.log(data)
  }

  const handleSubmit = (e)=>{
    e.preventDefault()
    submitData(title, author, genre, image)
    
    
  }

  return (
    <section className="text-gray-600 body-font relative">
      <div className="container px-5 py-24 mx-auto flex sm:flex-nowrap flex-wrap">
        <form onSubmit={handleSubmit} className=" bg-white flex flex-col md:ml-auto w-full md:py-8 mt-8 md:mt-0">
          <h2 className="text-gray-900 text-lg mb-1 font-medium title-font">
            Create Book
          </h2>
          <div className="relative mb-4">
            <label  className="leading-7 text-sm text-gray-600">
              Title
            </label>
            <input
              type="text"
              id="title"
              name="title"
              onChange={(e) => setTitle(e.target.value)}
              className="w-full bg-white rounded border border-gray-300 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out"
            />
          </div>
          <div className="relative mb-4">
            <label  className="leading-7 text-sm text-gray-600">
              Author
            </label>
            <input
              type="text"
              id="author"
              name="author"
              onChange={(e) => setAuthor(e.target.value)}
              className="w-full bg-white rounded border border-gray-300 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out"
            />
          </div>

          <div className="relative mb-4">
            <label className="leading-7 text-sm text-gray-600">
              Genre
            </label>
            <input
              type="text"
              id="genre"
              name="genre"
              onChange={(e)=>setGenre(e.target.value)}
              className="w-full bg-white rounded border border-gray-300 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out"
            />
          </div>

          <div className="relative mb-4">
            <label  className="leading-7 text-sm text-gray-600">
              Image Link
            </label>
            <input
              type="text"
              id="image"
              name="image"
              onChange={(e)=>setImage(e.target.value)}
              className="w-full bg-white rounded border border-gray-300 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out"
            />
          </div>

          <button className="text-white bg-indigo-500 border-0 py-2 px-6 focus:outline-none hover:bg-indigo-600 rounded text-lg">
            Submit
          </button>
        </form>
      </div>
    </section>
  );
};

export default CreateBook;

import { useEffect, useState } from "react";
import NavBar from "./components/NavBar";

function App() {
  const [books, setBooks] = useState([]);

  const fetchBooks = async () => {
    const response = await fetch("http://localhost:8080/books");
    const data = await response.json();
    setBooks(data);
  };

  useEffect(() => {
    fetchBooks();
  }, []);

  return (
    <>
      <NavBar />
      <section className="text-gray-600 body-font">
        <div className="container px-5 py-24 mx-auto">
          {books.map((book) => {
            return (
              <div key={book._id} className="flex flex-wrap -m-4">
                <div className="xl:w-1/4 md:w-1/2 p-4">
                  <div className="bg-gray-100 p-6 rounded-lg">
                    <img
                      className="h-40 rounded w-full object-cover object-center mb-6"
                      src={book.image}
                      alt="content"
                    />
                    <h3 className="tracking-widest text-indigo-500 text-xs font-medium title-font">
                      {book.author}
                    </h3>
                    <h2 className="text-lg text-gray-900 font-medium title-font mb-4">
                      {book.title}
                    </h2>
                    <p>{book.genre}</p>
                  </div>
                </div>
              </div>
            );
          })}
        </div>
      </section>
    </>
  );
}

export default App;

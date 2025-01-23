const bookList = document.getElementById("book-list");

async function getBooks() {
    const res = await fetch("http://localhost:8080/book/");
    
    if (!res.ok){
        alert("error with the server")
        return         
    }

    const books = res.json();

    books.forEach((book) => {
        const li = getBookElement(book);
        bookList.push(li);
    })
}

function getBookElement(book){
    const li = document.createElement("li");
    li.innerHTML = `
        <div class="flex flex-row gap-4">
            <div class="flex flex-col">
                <h2 class="text-xl font-bold">${book.title}</h2>
                <p class="text-sm">${book.author}</p>
                <p class="text-sm">${book.year}</p>
                <p class="text-sm">${book.genre}</p>
            </div>
            <div class="flex flex-col gap-2">                
                <button class="bg-red-500 text-white p-2 rounded-md">Delete</button>
            </div>
        </div>
    `

    li.getElementsByTagName("button")[0].addEventListener("click", () => {
        deleteBook(book.id);
    })

    return li;
}

getBooks();
import { useEffect, useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import { Link, useNavigate } from 'react-router-dom'

function App() {
  const [products, setProducts] = useState([])
  const navigate = useNavigate()

  const goToAbout = () =>  {
    navigate("/about", {data: "value"})
  }

  useEffect(() => {
    fetch("https://fakestoreapi.com/products")
    .then((res) => res.json())
    .then((prods) => setProducts(prods))
    .catch((err) => console.log(err))
  }, [])

  return (
    <main className="home">
      <h2>
        Home
      </h2>

      <ul>
        {products.map((product) => (
          <li>
            <div>
              <p> {product.title} </p>
              <Link 
                to={`/product/${product.id}`}
                state={product}
              >
                &rarr;
              </Link>
            </div>
          </li>
        ))}
      </ul>

      <button onClick={goToAbout}>
        Click
      </button>
    </main>
  )
}

export default App

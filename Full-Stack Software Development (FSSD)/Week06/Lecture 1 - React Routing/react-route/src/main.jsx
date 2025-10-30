import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
// import { createBrowserRouter, RouterProvider } from "react-router-dom"
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import App from './App.jsx'
// import AboutUs from './pages/AboutUs.jsx'
// import Contact from './pages/Contact.jsx'
// import "./index.css"
import NavBar from './components/NavBar.jsx'
import Product from './pages/Product.jsx'


// const paths = createBrowserRouter([
//   {
//     path: "/",
//     element: <App />,
//   },
//   {
//     path: "/contact",
//     element: <Contact />
//   },
//   {
//     path: "/about",
//     element: <AboutUs />
//   }
// ])

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <BrowserRouter>
      {/* <NavBar/> */}

      <Routes>
        <Route path='/' element={<App/>}  />     
        <Route path='/product/:id' element={<Product/>}  />        
      </Routes>
    </BrowserRouter>
  </StrictMode>,
)

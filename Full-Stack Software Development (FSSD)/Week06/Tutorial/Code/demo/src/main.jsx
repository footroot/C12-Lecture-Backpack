import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './styles/index.css' 
import App from './pages/App.jsx'
import Page1 from './pages/Page1.jsx'
import Page2 from './pages/Page2.jsx'
import { createBrowserRouter, RouterProvider } from 'react-router-dom'


const paths = createBrowserRouter([
  {
    path: '/',
    element: <App></App>
  },
  {
    path: '/page1',
    element: <Page1></Page1>
  },
  {
    path: '/page2',
    element: <Page2></Page2>
  }
]);


createRoot(document.getElementById('root')).render(
  <StrictMode>
    <RouterProvider router = {paths}/>
  </StrictMode>,
)

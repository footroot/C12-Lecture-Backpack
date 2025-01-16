import '../styles/App.css'
import NavBar from '../component/NavBar'
import { userContext } from '../context/userContext'

function App() {
  
  return (
  <>
    <userContext.Provider value = "Zahra">
      <NavBar></NavBar>
      <h1> This is the Home page!</h1>
    </userContext.Provider>
  </>
  )
}

export default App

import { Route, Routes } from 'react-router-dom'
import NavBar from './components/NavBar'
import Dashboard from './pages/Dashboard'
import Login from './pages/Login'
import { AuthContext } from './context/AuthContext'
import { useState } from 'react'

function App() {
  const [userDetails, setUserDetails] = useState(null);

  return (
    <>

      {/* NEW */}
      <AuthContext.Provider value={userDetails}>        
        
        <NavBar />        

        <Routes>
          <Route path="/" element={<h1>Home Page</h1>} />
          
          <Route path="/dashboard" element={<Dashboard />} />

          {/* Updated */}
          <Route path="/login" element={<Login setUserDetails={setUserDetails} />} />          
        </Routes>
      </AuthContext.Provider>
    </>
  )
}

export default App






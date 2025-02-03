
import { useState } from 'react'
import './App.css'

function App() {

  const [ username, setUsername ] = useState('')
  const [ password, setPassword ] = useState('')

  const [ resources, setResources ] = useState('')

  const handleLogin = async (e)=>{
    e.preventDefault()
    const response = await fetch('http://localhost:8080/login', {
      method: 'POST',
      headers: {
        'Content-Type' : 'application/json'
      },
      body: JSON.stringify({username: username, password: password})
    })
    const data = await response.json()
    console.log(data)
    localStorage.setItem('token', data.token)
  }

  const handleResourceView = async ()=>{
    const response = await fetch('http://localhost:8080/resource',{
      method: 'GET',
      headers: {
        Authorization : `Bearer ${localStorage.getItem('token')}`
      }
    })
    const data = await response.json()

    console.log(data)
  }


  return (
    <>
      <form onSubmit={handleLogin}>
        <input type='text' onChange={(e)=>setUsername(e.target.value)}/>
        <input type='password' onChange={(e)=>setPassword(e.target.value)}/>
        <button>Submit</button>
      </form>

      <button onClick={handleResourceView}>Get resources</button>
    </>
  )
}

export default App

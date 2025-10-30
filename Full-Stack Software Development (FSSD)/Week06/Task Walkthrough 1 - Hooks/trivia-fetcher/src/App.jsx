import { useEffect, useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'

function App() {
  const [currentNumber, setCurrentNumber] = useState(0)
  const [message, setMessage] = useState(undefined)

  useEffect(() => {
    fetch(`http://numbersapi.com/${currentNumber}`)
    .then((res) => res.text())
    .then((value) => setMessage(value))
    .catch((e) => console.log(e))

  }, [currentNumber])

  const handleNumberChange = (value) => {

    const number = Number(value);

    if (Number.isNaN(number)){
      setMessage(undefined)
      return
    }      

    setCurrentNumber(number)    
  }

  return (
    <>
      <p>
        {message ? message : "Please enter a number in the input box"}
      </p>

      <input type="number" onChange={(e) => handleNumberChange(e.target.value)} defaultValue={0} />
      
    </>
  )
}

export default App

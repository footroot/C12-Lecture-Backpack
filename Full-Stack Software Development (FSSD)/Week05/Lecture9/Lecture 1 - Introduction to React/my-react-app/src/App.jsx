import './App.css'
import MyButton from './components/MyButton.jsx';

function App() { 
  const message = 'Hello everyone';
  const classData = 'heading_text';   

  return (
    <>
      <h1 className="" style={{backgroundColor: "red"}}>
        {message}
      </h1>

      <MyButton value="Click me" onClick={() => alert("Hello!")} />
    </>
  )
}

export default App

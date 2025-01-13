import { useState } from "react";
import Names from "./components/Names";

function App() {
  const [name, setName] = useState("John Doe");

  const handleNameChange = ()=>{
    setName("James")
  }

  const handleTextChange = (e)=>{
    console.log(e.target.value)
  }

  const handleSubmit = (e)=>{
    e.preventDefault()
    console.log("Form has been submitted")
  }
  return (
    <>
      <Names value={name} />

      <button onClick={handleNameChange}>Change Name</button>

      <input onChange={handleTextChange}/>

      <form onSubmit={handleSubmit}>
        <input />

        <button>Submit</button>
      </form>
    </>
  );
}

export default App;

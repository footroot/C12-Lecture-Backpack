import { useState } from 'react'
import './App.css'
import Welcome from './Welcome';
import nameContext from './userContext';

function App() {
  let name = prompt("What is your name?");

  return (
    <nameContext.Provider value = {name}>
      <Welcome></Welcome>
    </nameContext.Provider>
      
  )
}

export default App

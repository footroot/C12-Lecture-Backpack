import { useState, useEffect } from "react";
import Ref from "./components/Ref";

/**
 *
 * useState = handle local state management
 * useEFfect = handle side effects in the component
 */

//95c9a67e

function App() {
  /**
   * movies - state variable = []
   * setMovies - state function
   * [] - intial value
   */
  const [movies, setMovies] = useState([])

  const [ count, setCount ] = useState(0)

  const fetchMovies = async () => {
    // A function that fetched movie information from the OMDB api
    const response = await fetch(
      "http://www.omdbapi.com/?s=harry&apikey=95c9a67e"
    );
    const data = await response.json();
    setMovies(data.Search);
  };

  useEffect(() => {
    fetchMovies(); // side effect
    //Dependancy array-> What determines when the side effect should be performed
}, []);

  console.log(movies)

  return (
    <>
    <Ref/>
    <button onClick={()=>setCount(count + 1)}>Increment Count</button>
      {
        movies.map((movie, index) =>{
          return (
            <div>
              <img src={movie.Poster}/>
              <p>{movie.Authors}</p>
            </div>
          )
        })
      }
    </>
  );
}

export default App;

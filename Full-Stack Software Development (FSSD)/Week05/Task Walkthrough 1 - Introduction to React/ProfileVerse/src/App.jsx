import { useState, useEffect } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import ProfileBanner from './components/ProfileBanner.jsx'
import SuggestedUsers from './components/SuggestedUsers.jsx'

function App() {
  const [data, setData] = useState([]);
  const [currentUser, setCurrentUser] = useState({});

  useEffect(() => {
    getData().then(data => setData(data));
    setCurrentUser(data[0]);
  }, []);

  console.log(currentUser);


  return (
    <main className="flex gap-10 w-full h-screen">
      <ProfileBanner {...currentUser} />
      <SuggestedUsers users={data} />
      
    </main>
  )
}

async function getData(){
  const response = await fetch('https://dummyapi.online/api/social-profiles');
  const data = await response.json();
  console.log(data);
  return data;
}

export default App

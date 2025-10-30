import NavBar from "../component/NavBar";
import { useName } from "../context/userContext";

function Page1() {
    const user = useName();

    return (
        <>
            <NavBar></NavBar>
            <h1> This is Page 1 </h1>
            <p> Welcome, {user}</p>
        </>
    )
}

export default Page1;
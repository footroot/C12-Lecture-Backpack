import { Link } from "react-router-dom";

function NavBar () {
    return (
        <>
            <Link to='/'>Home</Link>
            <Link to="/page1">Page 1</Link>
            <Link to="/page2">Page 2</Link>
        </>
    )
}

export default NavBar;
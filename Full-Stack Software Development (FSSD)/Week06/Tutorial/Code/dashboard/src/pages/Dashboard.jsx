import { useContext } from "react";
import { AuthContext } from "../context/AuthContext";

export default function Dashboard() {
    const userDetails = useContext(AuthContext);

    return (
        <>
            {
                userDetails ?
                    (
                        <div>
                            <h1>Welcome {userDetails.username}</h1>
                            <p>Your age is {userDetails.age}</p>
                            <p>Your favorite color is {userDetails.favoriteColor}</p>
                            <p>Your job title is {userDetails.jobTitle}</p>
                        </div>
                    ) :
                    (
                        <h1>Please login</h1>
                    )
            }
        </>
    )
}



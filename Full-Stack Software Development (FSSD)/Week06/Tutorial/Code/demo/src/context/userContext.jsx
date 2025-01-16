import { createContext } from "react";
import { useContext } from "react";

const userContext = createContext("");

export function useName() {
    return useContext(userContext);
}

export default userContext;

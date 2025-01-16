import { createContext, useContext } from 'react';

const nameContext = createContext("");

export function useName() {
    return useContext(nameContext);
}

export default nameContext;
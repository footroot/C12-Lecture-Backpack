import { useRef, useState, useEffect } from "react"
const Ref = ()=>{

    const paragraphRef = useRef()
    const container = useRef()
    const count = useRef(0)
    const [ countState, setCount ] = useState(0)

    const handleCountState = ()=>{
        setCount(countState + 1)
    }

    const handleCount = ()=>{
        count.current = count.current + 1
        console.log(count.current)

    }

    console.log("Componet rerendered")

    useEffect(()=>{
        paragraphRef.current.style.color = "blue"
    }, [])

    return (
        <>
        <button onClick={handleCount}>Handle Count</button>
        <button onClick={handleCountState}>Handle CountState</button>

        <p ref={paragraphRef}>Hello World</p>

        <div ref={container}>

        </div>
        </>
    )
}

export default Ref
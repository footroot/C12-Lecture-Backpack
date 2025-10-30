function MyButton({ value, onClick }) {
    const styling = {
        backgroundColor: "blue",
        border: "5px solid black",
        color: "white",
        padding: "10px",
        height: "150px",
        width: "300px"
    }

    return (
        <button onClick={onClick} style={styling}>
            {value}
        </button>
    )
}

export default MyButton
const express = require('express') // Importing Express
const app = express() // Initializing Express


app.listen(8080, ()=>{
    console.log('Server is running at port http://localhost:8080')
})

app.get('/', (req, res)=>{
    //data to be sent in json
    res.send("Cogrammar!!!!!")
})
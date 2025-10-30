import express from "express"

const app = express()

app.use((req, res, next)=>{
    console.log(`User has accessed ${req.method} ${req.url}`)
    next()
})

app.listen(8080, ()=>{
    console.log('Listening to port 8080')
})

app.get('/home', (request, response)=>{
    response.send("Hello")
})

app.get('/user/:name', (req, res)=>{
    res.send(`User Number: ${req.params.name}`)
})

/**
app.post()
app.put()
app.delete()
app.patch()
 */

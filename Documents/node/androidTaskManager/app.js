const http = require('http');
const express = require('express');
const app = express()

const hostname = '127.0.0.1';
const port = 3000;

app.get('/start', (req  , res ) => {
  res.send("Welcome Here")
})

app.get('/', (req , res) => {
  res.send("Here is the first Page")
} )

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`)
})
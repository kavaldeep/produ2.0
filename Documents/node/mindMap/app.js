const express = require('express')
const app = express()
const bodyParser  = require('body-parser');
const dbUtilis = require('./DatabaseUtilis');
 
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended: true}));

app.get('/',  (req, res) => {
  res.send('Hello World')
})
 

app.post('/saveNode' ,(req ,res) => 
{
  console.log(req.body);
  dbUtilis.saveNode(req , res);
})

app.post('/updateNodeArround' , (req , res ) => {
  dbUtilis.updateNodeArround(req , res);
})


app.get('/fetch' ,  (req , res) => {
dbUtilis.fetch(res);
})
app.listen(3000)

const http = require('http');
const express = require('express');
const app = express()
const bodyParser  = require('body-parser');
const mongoose = require('./utilis/mongoose')
const monAnalytics = require('./utilis/monAnalytics')

const hostname = '127.0.0.1';
const port = 3000;


app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended: true}));

app.get('/start', (req  , res ) => {
  res.send("Welcome Here")
})

app.get('/', (req , res) => {
  res.send("Here is the first Page")
} )

app.post('/create' , (req , res) =>{
  console.log("This is the Body :" ,  req.body)
  mongoose.postSave(req)
  res.send("attempt To Save")
})

app.post('/fetchByDate' , (req , res) => {

  console.log(req.body.Date)
  mongoose.fetchDataByDate(req.body.Date , res)
  res.send("recived")

})

app.post('/fetchToDay' , (req , res) => {

  console.log("Fetching for today")
  mongoose.fetchDataToday(res)
})


app.post('/delete' , (req , res) =>
{
  console.log("Asking To Delte")
  mongoose.deleteById(req , res) 
})

app.post('/update' , (req , res) => 
{
  console.log("Asking to update")
  mongoose.updateById(req , res)
})

app.post('/updateTime' , (req , res) => {
  console.log("Asking To update the Time for the id : " ,  req.body._id)
  console.log(req.body)
  monAnalytics.updateTime(req , res ) 
})

app.post('/fetchDataTime' , (req , res) => {
  console.log("Asking for fetch dataTime for the id :")
  monAnalytics.fetchData(req , res)
})

app.listen(process.env.PORT || 3000, 
	() => console.log("Server is running..."));
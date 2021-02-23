const mongoose  = require('mongoose')
const workAnalytics = require('../models/workAnalytics')
const {workAnalyticsModel , startAndEndModel } = require('../models/workAnalytics')
const datePlusOne = require('../utilis/mongoose').datePlusOne

const saveData = (data) => { 
    mongoose.connect('mongodb+srv://kavaldeep:kavaldeep@cluster0.fgywy.mongodb.net/toDoList?retryWrites=true&w=majority' , {
        useNewUrlParser : true , 
        useCreateIndex : true 
        })
    
        data.save().then((result) => {
            console.log(result)
        }).catch((error) =>{
            console.log(error)
        }) 
}

const create = (id) => {
    //id = 6026afa1d20f8b0004c53548
    mongoose.connect('mongodb+srv://kavaldeep:kavaldeep@cluster0.fgywy.mongodb.net/toDoList?retryWrites=true&w=majority' , {
        useNewUrlParser : true , 
        useCreateIndex : true 
        })

        const emptyModel = new workAnalyticsModel({
            _id : mongoose.Types.ObjectId(id)
        })

        emptyModel.save().then((result) => {
            console.log(result)
        }).catch((err) => { 
            console.log(err)
        })
    }
    
const updateTime = (req , res) => {
        mongoose.connect('mongodb+srv://kavaldeep:kavaldeep@cluster0.fgywy.mongodb.net/toDoList?retryWrites=true&w=majority' , {
        useNewUrlParser : true , 
        useCreateIndex : true 
        })

        workAnalyticsModel.updateOne({
           _id : mongoose.Types.ObjectId(req.body._id)
        },{
            "$push":{
                workHistory: new startAndEndModel({
                    startTime : req.body.startTime , 
                    endTime: req.body.endTime
                })
            }
        }
        ).then((result) => {
            console.log(result)
            res.send("time Info Saved ")
        }).catch((err) => {
            console.log(err)
            res.send("Unable To Save")
        })
}

const fetchData = (req , res) => {
    mongoose.connect('mongodb+srv://kavaldeep:kavaldeep@cluster0.fgywy.mongodb.net/toDoList?retryWrites=true&w=majority' , {
        useNewUrlParser : true , 
        useCreateIndex : true 
        })

        workAnalyticsModel.findOne({ _id : mongoose.Types.ObjectId(req.body._id)}).then((result) => {
            res.send(result)
        }).catch((error) => {
            res.send(error)
        })
}

const chartToday = (res) => {
    mongoose.connect('mongodb+srv://kavaldeep:kavaldeep@cluster0.fgywy.mongodb.net/toDoList?retryWrites=true&w=majority' , {
        useNewUrlParser : true , 
        useCreateIndex : true 
        })

        const wa = new workAnalyticsModel();
        var dateToday = new Date()
        var gte = dateToday.toISOString().split("T")[0]
        var lte = datePlusOne(new Date())
        console.log(gte , lte)
    
        workAnalyticsModel.find({
            "workHistory.endTime" : {
                "$gte" : gte , "$lt" : lte
            }
        }).then((result) => {

          for(var i = 0 ; i < result.length ; i++)
            {
               for(var j = 0 ; j < result[i].workHistory.length ; j++)
               {
                   console.log((result[i].workHistory[j].endTime));
                   if(result[i].workHistory[j].endTime.getDate() == 23)
                   {
                    
                    wa.workHistory.push(result[i].workHistory[j])
                    console.log("Done")
                   }
               }
            }
            res.send(wa);
        }).catch((err) =>{
            res.send(err);
            console.log(err);
        })

}

module.exports  = {create , updateTime , saveData , fetchData , chartToday } 



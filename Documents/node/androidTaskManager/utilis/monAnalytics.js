const mongoose  = require('mongoose')
const workAnalytics = require('../models/workAnalytics')
const {workAnalyticsModel , startAndEndModel } = require('../models/workAnalytics')


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
module.exports  = {create , updateTime , saveData , fetchData} 



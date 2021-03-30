const mongoose  = require('mongoose')
const workAnalytics = require('../models/workAnalytics')
const {workAnalyticsModel , startAndEndModel } = require('../models/workAnalytics')
//const datePlusOne = require('../utilis/mongoose').datePlusOne

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

const chartDate = (req  , res) => {
    //Excpected Date Format 2021-02-11
    mongoose.connect('mongodb+srv://kavaldeep:kavaldeep@cluster0.fgywy.mongodb.net/toDoList?retryWrites=true&w=majority' , {
        useNewUrlParser : true , 
        useCreateIndex : true 
        })

        const wa = new workAnalyticsModel();
        var dateToFind = stringToDate(req.body.date);
        var gte = dateToFind.toISOString().split("T")[0]
        var lte = datePlusOneX(dateToFind);
        workAnalyticsModel.find({
            "workHistory.endTime" : {
                "$gte" : gte , "$lt" : lte
            }
        }).then((result) => {
          for(var i = 0 ; i < result.length ; i++)
            {
               for(var j = 0 ; j < result[i].workHistory.length ; j++)
               {
                   console.log((result[i].workHistory[j].endTime) , dateToFind.getDate());
                //possible qu on continue la tache apres miniuit if(result[i].workHistory[j].endTime.getDate() == dateToFind.getDate())
                    wa.workHistory.push(result[i].workHistory[j])
                    console.log("Done")
                }
            }
            res.send(wa);
        }).catch((err) =>{
            console.log(err);
        })
}

const datePlusOneX = (date) => {
    date.setDate(date.getDate() + 1 )
    return date.getFullYear() + "-" + (date.getMonth() + 1 ) + "-" + date.getDate() ;
}


const stringToDate = (date) =>{
    console.log(date);
    switch(date.length){
        case 10:
            var parts = date.split('-');
            break;
        default:
            var parts = date.split('T')[0].split('-');
            break;
    }
    console.log(parts);    
    var  date = new Date();
    date.setDate(parts[0]);
    date.setYear(parts[2]);
    date.setMonth(parts[1] - 1 );
    return date;
}

module.exports  = {create , updateTime , saveData , fetchData , chartDate } 



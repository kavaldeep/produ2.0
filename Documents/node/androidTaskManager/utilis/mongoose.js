const mongoose  = require('mongoose')
const Task = require('../models/task')

const saveTask = (task) => {
    mongoose.connect('mongodb+srv://kavaldeep:kavaldeep@cluster0.fgywy.mongodb.net/toDoList?retryWrites=true&w=majority' , {
    useNewUrlParser : true , 
    useCreateIndex : true 
    })

    task.save().then((result) => {
        console.log("succes")
    }).catch((error) => {
        console.log("Failed To Save")
        console.log(error)
    })
}

const postSave = (req) => {
    
    const newTask = new Task({
        Description :  req.body.Description ,
        Priority : Number(req.body.Priority),
        DeadLine : Date.now(),
        State : req.body.State ,
        Duration : req.body.Duration,
        CreationDate : Date.now()
    })

    saveTask(newTask)
}

const fetchDataByDate = (date , res )  => {
    mongoose.connect('mongodb+srv://kavaldeep:kavaldeep@cluster0.fgywy.mongodb.net/toDoList?retryWrites=true&w=majority' , {
    useNewUrlParser : true , 
    useCreateIndex : true 
    })
    //TODO Complete This Properly
/*   
    Task.find({ DeadLine : { "$gte" : "2021-02-11 ", "$lt" : "2021-02-12" } } , (err , data) => {
        if(err){
            console.log(err)
        }else{
        }
    }) */

}

const fetchDataToday = (res) =>{
    mongoose.connect('mongodb+srv://kavaldeep:kavaldeep@cluster0.fgywy.mongodb.net/toDoList?retryWrites=true&w=majority' , {
    useNewUrlParser : true , 
    useCreateIndex : true 
    })
    
    var dateToday = new Date()
    var gte = dateToday.toISOString().split("T")[0]
    var lte = datePlusOne(new Date())
    console.log(gte , lte)

    Task.find({CreationDate : { "$gte" : gte , "$lt": lte  }} , (err , data ) => {
        if(err){
            console.log(err)
        }else{
            res.send(data)
        }
    })
    
    
}


const deleteById = (req , res) =>{
    mongoose.connect('mongodb+srv://kavaldeep:kavaldeep@cluster0.fgywy.mongodb.net/toDoList?retryWrites=true&w=majority' , {
    useNewUrlParser : true , 
    useCreateIndex : true 
    })

    Task.find({_id : mongoose.Types.ObjectId(req.body._id)} , (err , data)=> {
        if(err){
            console.log(err)
        }else{
            console.log(data)
        }
    })
    
    Task.deleteOne({_id :  mongoose.Types.ObjectId(req.body._id)} , (err , result) =>{
        console.log(req.body._id);
        if(err){
            res.send("unable To Delete")
        }else{
            res.send("Succes Delete")
            console.log(result)
        }
    })
}

const updateById = (req , res) => {
    
    mongoose.connect('mongodb+srv://kavaldeep:kavaldeep@cluster0.fgywy.mongodb.net/toDoList?retryWrites=true&w=majority' , {
    useNewUrlParser : true , 
    useCreateIndex : true 
    })

    console.log(req.body._id)
    Task.updateOne({_id :mongoose.Types.ObjectId(req.body._id)} , ({$set : { Description : req.body.Description , 
        Priority : Number(req.body.Priority),
        DeadLine : stringToDate(req.body.DeadLine) ,
        State : req.body.State ,
        Duration : req.body.Duration,
        CreationDate : Date.now() , 
    }}) , (err , result) =>{
        if(err)
        {
            console.log(err)
        }else{
            console.log(result)
        }
    }) 

    res.send("update Request Recived");

}
const datePlusOne = (date) => {
    date.setDate(date.getDate() + 1 )
    return date.getFullYear() + "-" + (date.getMonth() + 1 ) + "-" + date.getDate() ;
}

const stringToDate = (date) =>{
    var parts = date.split('-');    
    return new Date(parts[0], parts[1] - 1, parts[2])
}


module.exports = {saveTask , postSave , fetchDataByDate , fetchDataToday , deleteById , updateById}


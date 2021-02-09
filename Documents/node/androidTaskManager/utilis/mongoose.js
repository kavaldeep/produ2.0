const mongoose = require('mongoose')
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
    })

    saveTask(newTask)
}





module.exports = {saveTask , postSave}


const mongoose = require('mongoose')

const saveTask = (task) => {
    mongoose.connect('mongodb+srv://kavaldeep:kavaldeep@cluster0.fgywy.mongodb.net/toDoList?retryWrites=true&w=majority' , {
    useNewUrlParser : true , 
    useCreateIndex : true 
    })

    task.save().then((result) => {
        console.log("succes")
    }).catch((error) => {
        console.log("Failed To Save")
    })
}


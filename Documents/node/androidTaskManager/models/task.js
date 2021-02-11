const mongoose = require('mongoose')

const TaskSchema = mongoose.model('Task', {
    Description : {
        type : String ,
        required: true,
        valdation: (value) => {
            return value.toUpperCase() 
        }
    },

    Priority : {
        type : Number
    },

    DeadLine : {
        type : Date
    },

    State : {
        type : String
    },

    Duration : {
        type : String
    },
    
    CreationDate : 
    {
        type : Date
    }
})


module.exports = TaskSchema.model("Task", TaskSchema) 
const mongoose = require('mongoose')

const Task = mongoose.model('Task', {
    Descrption : {
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
    }
})

module.exports = Task
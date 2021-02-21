const mongoose = require('mongoose')


 const startAndEnd =  mongoose.Schema({
    startTime: Date,
    endTime: Date
})

const workAnalytics = mongoose.Schema({
    workHistory: [startAndEnd]
})
 
const workAnalyticsModel  = mongoose.model("workAnalytic" , workAnalytics)
const startAndEndModel = mongoose.model("notImportant"  , startAndEnd )

module.exports = {workAnalyticsModel , startAndEndModel}

const mongoose  = require('mongoose')

const Node  = mongoose.model('nodes',{
/*     Ca c est super Obselete
 */    shape: Number,
    color:Number,
    nodesArround : [String],
    position : {
        x:Number,
        y:Number,
        z:Number
    },
    height:Number,
    image:String,
    text:{
        text:String
    },
})

const nodeSchema = mongoose.Schema({
    shape: Number,
    color:{
        r:Number,
        g:Number,
        b:Number,
        a:Number
    },
    nodesArround : [String],
    position : {
        x:Number,
        y:Number,
        z:Number
    },
    height:Number,
    image:String,
    text:{
        text:String
    },
    icon:{
        prefabName:String
    },
    line:{
        color:{
            r:Number,
            g:Number,
            b:Number,
            a:Number
        },
        width:Number,
    }
})
const postSave = (req) => {
    const modelSave = mongoose.model(req.body.room , nodeSchema)
    const nodeToSave = new modelSave({
        shape: req.body.shape,
        color : {
            r:req.body.color.r,
            g:req.body.color.g,
            b:req.body.color.b,
            a:req.body.color.a,

        },
        position:{
            x:req.body.position.x,
            y:req.body.position.y,
            z:req.body.position.z
        },
       
        height: req.body.height,
        image: req.body.image,
        text:{
            text:req.body.text.text
        },
        icon:{
            prefabName:req.body.icon.prefabName
        },
        line:{
            color: {
                r:req.body.line.color.r,
                g:req.body.line.color.g,
                b:req.body.line.color.b,
                a:req.body.line.color.a,
            },
            width: req.body.line.width,
        }
    })

    return nodeToSave
}
const saveNode = ( req , res ) => {
    mongoose.connect('mongodb+srv://kavaldeep:kavaldeep@cluster0.fgywy.mongodb.net/toDoList?retryWrites=true&w=majority' , {
    useNewUrlParser : true , 
    useCreateIndex : true 
    })
    const node = postSave(req)
    node.save().then((result) => {
        console.log(result)
        res.send("Node Saved")
    }).catch((error) => {
        console.log(error);
        res.send("Node Saved")
    }) 
}
const updateNodeArround = (req , res) => {
    mongoose.connect('mongodb+srv://kavaldeep:kavaldeep@cluster0.fgywy.mongodb.net/toDoList?retryWrites=true&w=majority' , {
        useNewUrlParser : true , 
        useCreateIndex : true 
        })
    const nodeUpdate = mongoose.model(req.body.room , nodeSchema);
    nodeUpdate.updateOne({_id : mongoose.Types.ObjectId(req.body.ida)} , ({
        "$push" : {
                nodesArround : mongoose.Types.ObjectId(req.body.idb)
    }})).then((result) => {
        console.log(result)
        res.send(result)
    }).catch((error) => {
        console.log(error)
        res.send(error)
    })

    nodeUpdate.updateOne({_id : mongoose.Types.ObjectId(req.body.idb)} , ({
        "$push" : {
                nodesArround : mongoose.Types.ObjectId(req.body.sssdaida)
    }})).then((result) => {
        console.log(result)
    }).catch((error) => {
        console.log(error)
    })
}


const fetch = (res) =>{
    mongoose.connect('mongodb+srv://kavaldeep:kavaldeep@cluster0.fgywy.mongodb.net/toDoList?retryWrites=true&w=majority' , {
        useNewUrlParser : true , 
        useCreateIndex : true 
        })

    Node.find({}).then((result) => {
        
        res.send(arrangeString(result))
    }).catch((error) => {
        console.log(error);
        res.send(error);
    })
}


const arrangeString = (result) => {

    var resultReturn = "";
    for(var i = 0 ; i < result.length ; i++)
    {
        resultReturn = resultReturn + result[i] + "|";
    }
    console.log(resultReturn);
    return resultReturn;
}

module.exports = {saveNode , postSave , updateNodeArround , fetch}

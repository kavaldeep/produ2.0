from pymongo import MongoClient
from agile.models import Task
from datetime import datetime
from django.http import HttpResponse , HttpResponseRedirect
from bson.objectid import ObjectId
from django.views.decorators.csrf import csrf_exempt
<<<<<<< HEAD
=======
import json
>>>>>>> 39d111bf061e4c3e2e8276a0abab7e369a515f83

def getTasks():
    """
    Get The Tasks of today 
    """
    print("getting taks")
<<<<<<< HEAD
    startDate = datetime(2021 , 6 , 8 , 0 , 0 , 0 )
    endDate = datetime(2021 , 6 ,  9 , 0 , 0 , 0 )
=======
    startDate = datetime(int(datetime.today().year) , int(datetime.today().month) , int(datetime.today().day) , 0 , 0 , 0 )
    endDate = datetime(int(datetime.today().year) , int(datetime.today().month) + 1  ,  int(datetime.today().day) , 0 , 0 , 0 )
    print("Getting task of the start " + str(startDate) + " and the end date is " + str(endDate))
>>>>>>> 39d111bf061e4c3e2e8276a0abab7e369a515f83
    client = MongoClient("mongodb+srv://kavaldeep:kavaldeep@cluster0.fgywy.mongodb.net/toDoList?retryWrites=true&w=majority")
    db = client.toDoList
    collection = db["tasks"]
    content = collection.find({"CreationDate" : { "$lte" : endDate  , "$gte" : startDate}})
    tasks = []
    for x in content:
        tasks.append(Task(x["Description"] , x['Priority'] , x['DeadLine'] , x['State'] , x['Duration'] , x['CreationDate'] , str(x['_id'])))
    return tasks

<<<<<<< HEAD

=======
>>>>>>> 39d111bf061e4c3e2e8276a0abab7e369a515f83
def getTime(pk):
    print("#Debug getting the time")
    return getCollection().find_one({'_id' : ObjectId(pk)})


def addTask(request):

    """
    To Add task
    """
    task = Task(request.POST.get("Contenue") , 4 , datetime.now() , convertState(request.POST.get("Etat")) , request.POST.get("TempsAConsacrer") , datetime.now())
    client = MongoClient("mongodb+srv://kavaldeep:kavaldeep@cluster0.fgywy.mongodb.net/toDoList?retryWrites=true&w=majority")
    database = client.toDoList
    collection = database["tasks"]
    addTask = collection.insert_one(task.__dict__)
    return HttpResponseRedirect('/agile')

def deleteTask(request):
    print("----------------------------------task delete pk = " + request.POST.get("pk"))
    client = MongoClient("mongodb+srv://kavaldeep:kavaldeep@cluster0.fgywy.mongodb.net/toDoList?retryWrites=true&w=majority")
    database = client.toDoList
    collection = database["tasks"]
    collection.delete_one({'_id' : ObjectId(request.POST.get("pk"))})    
    return HttpResponseRedirect('/agile')

@csrf_exempt
def updateFinish(request):
    print("-------------------update TO finsih with id = " +  request.POST.get("pk"))
    getCollection().update_one({ "_id" : ObjectId(request.POST.get("pk").replace(" ", ""))} , {"$set" : {"State" : "Finish"} })    
<<<<<<< HEAD
    return HttpResponseRedirect('/agile')
=======
    json_data = json.dumps({"HTTPRESPONSE":"ok"})
    return HttpResponse(json_data)
>>>>>>> 39d111bf061e4c3e2e8276a0abab7e369a515f83

@csrf_exempt
def updateInProgress(request):
    print("-------------------update To InProgress with id = " + request.POST.get("pk"))
    getCollection().update_one({ "_id" : ObjectId(request.POST.get("pk").replace(" ", ""))} , {"$set" : {"State" : "InProgress"} })    
<<<<<<< HEAD
    return HttpResponseRedirect('/agile')

=======
    json_data = json.dumps({"HTTPRESPONSE":"ok"})
    return HttpResponse(json_data)

#This code is to much fucking self explantory as fuck OMG 
>>>>>>> 39d111bf061e4c3e2e8276a0abab7e369a515f83
@csrf_exempt
def updateToDo(request):
    print("-------------------update To todo with id = " + request.POST.get("pk"))
    getCollection().update_one({ "_id" : ObjectId(request.POST.get("pk").replace(" ", ""))} , {"$set" : {"State" : "ToDo"} })    
<<<<<<< HEAD
    return HttpResponseRedirect('/agile')
=======
    json_data = json.dumps({"HTTPRESPONSE":"ok"})
    return HttpResponse(json_data)
>>>>>>> 39d111bf061e4c3e2e8276a0abab7e369a515f83

def updateTask():
    print("update task")


def testfunction():
    print("its on work baby -------------------------------------")


def convertState(state):
    print("#Debug ------------------The State is  " + state)
    stateToReturn = ""
    if(state == "A Faire"):
        stateToReturn = "ToDo"
    elif(state == "En Cours"):
        stateToReturn = "InProgress"
    elif(state == "Finis"):
        stateToReturn = "Finish"
    else:
        stateToReturn = "ToDo"

    return stateToReturn

<<<<<<< HEAD
=======

>>>>>>> 39d111bf061e4c3e2e8276a0abab7e369a515f83
def getCollection():
    print("***********getting Collection***********")
    client = MongoClient("mongodb+srv://kavaldeep:kavaldeep@cluster0.fgywy.mongodb.net/toDoList?retryWrites=true&w=majority")
    database = client.toDoList
    collection = database["tasks"]
<<<<<<< HEAD
    return collection

=======
    return collection
>>>>>>> 39d111bf061e4c3e2e8276a0abab7e369a515f83

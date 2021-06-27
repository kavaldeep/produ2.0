from pymongo import MongoClient
from agile.models import Task
from datetime import datetime
from django.http import HttpResponse , HttpResponseRedirect
from bson.objectid import ObjectId
from django.views.decorators.csrf import csrf_exempt
import json

def getTasks():
    """
    Get The Tasks of today 
    """
    print("getting taks")
    startDate = datetime(int(datetime.today().year) , int(datetime.today().month) , int(datetime.today().day) , 0 , 0 , 0 )
    endDate = datetime(int(datetime.today().year) , int(datetime.today().month) + 1  ,  int(datetime.today().day) , 0 , 0 , 0 )
    print("Getting task of the start " + str(startDate) + " and the end date is " + str(endDate))
    client = MongoClient("mongodb+srv://kavaldeep:kavaldeep@cluster0.fgywy.mongodb.net/toDoList?retryWrites=true&w=majority")
    db = client.toDoList
    collection = db["tasks"]
    content = collection.find({"CreationDate" : { "$lte" : endDate  , "$gte" : startDate}})
    tasks = []
    for x in content:
        tasks.append(Task(x["Description"] , x['Priority'] , x['DeadLine'] , x['State'] , x['Duration'] , x['CreationDate'] , str(x['_id'])))
    return tasks


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
    json_data = json.dumps({"HTTPRESPONSE":"ok"})
    return HttpResponse(json_data)

@csrf_exempt
def updateInProgress(request):
    print("-------------------update To InProgress with id = " + request.POST.get("pk"))
    getCollection().update_one({ "_id" : ObjectId(request.POST.get("pk").replace(" ", ""))} , {"$set" : {"State" : "InProgress"} })    
    json_data = json.dumps({"HTTPRESPONSE":"ok"})
    return HttpResponse(json_data)

#This code is to much fucking self explantory as fuck OMG 
@csrf_exempt
def updateToDo(request):
    print("-------------------update To todo with id = " + request.POST.get("pk"))
    getCollection().update_one({ "_id" : ObjectId(request.POST.get("pk").replace(" ", ""))} , {"$set" : {"State" : "ToDo"} })    
    json_data = json.dumps({"HTTPRESPONSE":"ok"})
    return HttpResponse(json_data)

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


def getCollection():
    print("***********getting Collection***********")
    client = MongoClient("mongodb+srv://kavaldeep:kavaldeep@cluster0.fgywy.mongodb.net/toDoList?retryWrites=true&w=majority")
    database = client.toDoList
    collection = database["tasks"]
    return collection
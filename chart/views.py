from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from tache_app.models import TacheTemps  , TempsDeTravail
import ast
import datetime
import json

# Create your views here. for charts
"""
faire avec les parametres jour et mois plus tard
"""
def retreive_hour_day_month_dict(TacheTemps , day , month ):
	"""
	retourne un dictionnaire  avec en cle l heur
	et en valeur le nombre de secondes
	"""
	timeList = []
	travailTable = {}
#	travailTable = [datetime.timedelta(0) for i in range(0 , 23)]

	for time in TacheTemps.objects.all():
		timeList.append(ast.literal_eval(time.TempsList))
	for x in range(0 , len(timeList) ) :
		timeList[x][0] = datetime.datetime.strptime(timeList[x][0][0:19] , '%Y-%m-%d %H:%M:%S' )
		timeList[x][1] = datetime.datetime.strptime(timeList[x][1][0:19] , '%Y-%m-%d %H:%M:%S' )
	timeList.sort()
	newList = [ a for a in timeList if a[0].day == day and a[0].month == month]
	for time in newList:
		travailTable[time[1].hour] = time[1] - time[0]

	for i in range(0 , 24):
		travailTable[i] = travailTable.get( i , datetime.timedelta(0))
	return dict(sorted(travailTable.items()))

def add_last_item_dict(travailTable):
	"""cette fonction va cumuler tous les heures pour a chque heure de
	la journee ou jour du mois pour les mettres dans le graphique
	"""
	newDict = {}
	lastValue = 0
	for key in travailTable.keys():
		newDict[key] = lastValue + travailTable[key].seconds/3600
		lastValue = newDict[key]
	return newDict

def reverse_dict(myDict):
	"""
	Cette fonction va inverser l ordre des cles dans les dictionnaire 
	"""
	newDict = {}
	listKey  = [key for key in myDict.keys()]
	for key in reversed(listKey):
		newDict[key] = myDict[key]
	return newDict

""" def chartToday(request):
	return render(request , 'chart.html' , {"labels" : list(add_last_item_dict(retreive_hour_day_month_dict(TacheTemps , datetime.date.today().day , datetime.date.today().month)).keys()) ,
	 "values" : list(add_last_item_dict(retreive_hour_day_month_dict(TacheTemps , datetime.date.today().day , datetime.date.today().month)).values()) })
 """
def chartMonth(request):
	MonthDict = {}
	for i in range(0 , 31):
		jour = datetime.date.today() - datetime.timedelta(days = i)
		MonthDict[jour.day] = list(add_last_item_dict(retreive_hour_day_month_dict(TacheTemps , jour.day , jour.month)).values())[-1]
	MonthDict = reverse_dict(MonthDict)
	return render(request , 'chartMonth.html' , {"labels" : list(MonthDict.keys()) , "values" :list((MonthDict.values()))})


def chartToday(request):

	liste = TempsDeTravail.dayData(datetime.date.today().day  , datetime.date.today().month)	
	label = []
	[label.append(i) for  i in range(0 , 23) ]
	return render(request , 'chart.html' , {"labels" : label , "values" : liste })
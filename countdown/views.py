
from django.shortcuts import render
from django.http import HttpResponse 
from django.template.loader import get_template
from tache_app.models import Tache
from django.utils import timezone
from datetime import timedelta
from agile import dbUtilis
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
"""
j ai pas le choix je sui obligé de mutliplié TempsAConsacrer pour le mettre en secondes 
temps a consacrer * 3600
"""


def countdown(request):
	time = 200
	return render(request , 'countdown.html' , {"time": time})

def countdownWith(request , pk):
	timeRestant = (Tache.objects.get(pk = pk).TempsAConsacrer)*3600 - Tache.objects.get(pk = pk).TempsConsacrer

	tache = Tache.objects.get(pk = pk)
	"""Lorsque la page charge on me PauseouPlay pour compter le temps de travail dans views tache_app""" 
	tache.PauseouPlay = 1
	tache.TempsTemp = timezone.now()
	tache.save()
	return render(request , 'countdown.html' , {"time": timeRestant , "pk" : pk})

def lancerCompteur(request , pk ):
	
	return render(request , 'countdown.html' , {"time":Tache.objects.get(pk = pk ).TempsRestant , "pk" : pk})	


def launchCountDown(request):
	#format hh:mm
	pk = "60dbe69e6aeb8fd0ba1a5860"
	print("#Debug asking for countdown Timer")
	return render(request , 'countdown.html' , {"time" : dbUtilis.getTime(pk)["Duration"] , "pk":pk})

@csrf_exempt
def postGetTime(request):
	if(request.method == "POST"):
		print(request.POST.get("_id"))
		print("#it is a post request asking for the time")
		json_data = json.dumps({"HTTPRESPONSE":"ok" , "time" : convertTimeToSeconds(dbUtilis.getTime(request.POST.get("_id").replace('"' , ""))["Duration"])})

		return HttpResponse(json_data)

	else:
		return render(request , 'not a good method ')		


def convertTimeToSeconds(time):
	#format hh:mm
	return int(time.split(":")[0]) * 60 * 60 + int(time.split(":")[1])*60 

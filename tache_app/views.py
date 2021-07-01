from django.shortcuts import render , get_object_or_404
from tache_app.forms import TacheForm , TacheFormAdd
from django.views.generic import CreateView , UpdateView , DeleteView
from tache_app.models import Tache , TacheTemps , TempsDeTravail
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse , HttpResponseRedirect
import json
from django.utils import timezone
import datetime 
from datetime import timedelta
from agile.models import Task
from pymongo import MongoClient
# Create your views here.

@csrf_exempt
def TimeUpdate(request):
	"""
	On va update le Time Tout les 60 sec 
	"""
	find = False
	 
	if(request.method == "POST"):
		identifiant = int(request.POST.get("pk"))
		tacheToUpdate = Tache.objects.get(pk = identifiant ) 
		tempsPasser  =  tacheToUpdate.TempsRestant - timedelta(seconds = int(request.POST.get("timeLeft")))
		print(tempsPasser)
		tacheToUpdate.TempsRestant = timedelta(seconds = int(request.POST.get("timeLeft")))
		tacheToUpdate.save()

		for elem in TempsDeTravail.objects.all()[::-1]:
			if elem.day.hour == datetime.datetime.now().hour :
				elem.deltaTemps = elem.deltaTemps + tempsPasser
				print("-----------")
				print(elem.deltaTemps)				
				elem.save()	
				find = True 
				break
	
		if not find:
			newElem = TempsDeTravail()
			newElem.day = datetime.datetime.now()
			newElem.deltaTemps =  tempsPasser
			
			newElem.save()

	json_data = json.dumps({"HTTPRESPONSE":"ok"})
	return HttpResponse(json_data)	
	
@csrf_exempt
def addToContenue(request):
	"""
	On a recu un post ajax on le traite ici
	a faire ecrire correctement le code pour changer le temps de la tache
	On va aussi les temps de travail a et b dans le model TacheTemps
	"""
	pk = int(request.POST['pk'])
	post = int(request.POST['message'])
	tacheAtraiter = Tache.objects.get(pk = pk)
	if tacheAtraiter.PauseouPlay == 1 and post ==  0:
		"""
		On passe de play a pause
		"""
		tacheAtraiter.TempsConsacrer +=  (timezone.now() - tacheAtraiter.TempsTemp).seconds
		tacheAtraiter.PauseouPlay = 0

		timeList = []
		timeList.append(str(tacheAtraiter.TempsTemp))
		timeList.append(str(timezone.now()))

		TempsSend = TacheTemps.objects.create(TempsList = json.dumps(timeList))
		print(TempsSend.TempsList)
		TempsSend.save()
		tacheAtraiter.TempsCle = tacheAtraiter.TempsCle + "," + str(TempsSend.id)
		tacheAtraiter.save()

	elif tacheAtraiter.PauseouPlay  == 0 and post == 1:
		"""La on passe de pause a play
		donc on etait en pause
		"""
		tacheAtraiter.PauseouPlay = 1
		tacheAtraiter.save()

	json_data = json.dumps({"HTTPRESPONSE":"ok"})
	return HttpResponse(json_data)

@csrf_exempt
def ChangeToEnCours(request ):
	pk = request.POST['pk']
	print("Change to Encours ------------------------" + pk)
	TacheATraiter =  Tache.objects.get(pk = pk)
	TacheATraiter.Etat = "En Cours"
	TacheATraiter.save()
	json_data = json.dumps({"HTTPRESPONSE":"ok"})
	return HttpResponse(json_data)
 
 
@csrf_exempt
def ChangeToAFaire(request):
	pk = int(request.POST['pk'])
	TacheATraiter =  Tache.objects.get(pk = pk)
	TacheATraiter.Etat = "A faire"
	TacheATraiter.save()
	json_data = json.dumps({"HTTPRESPONSE":"ok"})
<<<<<<< HEAD
=======
	print("the json data is " + json_data)
>>>>>>> 39d111bf061e4c3e2e8276a0abab7e369a515f83
	return HttpResponse(json_data)

@csrf_exempt
def ChangeToFinis(request):
	pk = int(request.POST['pk'])
	TacheATraiter =  Tache.objects.get(pk = pk)
	TacheATraiter.Etat = "Finis"
	TacheATraiter.FinishDate = timezone.now()
	TacheATraiter.save()
	json_data = json.dumps({"HTTPRESPONSE":"ok"})
<<<<<<< HEAD
=======
	print("the json data is " + json_data)
>>>>>>> 39d111bf061e4c3e2e8276a0abab7e369a515f83
	return HttpResponse(json_data)


def tache_ajouter(request):
	
	"""
	Ici on va s occuper de traiter la tache
	Cette fonction va etre appeler lorsque on va tenter d acceder a la page ajouter tache
	on va leur envoyer un formulaire TacheForm
	"""
	elem = Tache()
	if(request.method == "POST"):
		elem.Contenue = request.POST.get("Contenue")
		elem.Etat = request.POST.get("Etat")
		t =  datetime.datetime.strptime(request.POST.get("TempsAConsacrer")	, '%H:%M')
		elem.TempsAConsacrer =timedelta( hours = t.hour , minutes= t.minute)
		elem.TempsRestant = elem.TempsAConsacrer
		elem.save()


	"""
	Une fois le traitement fais la view va retourner les variables dans locals , et une page html
	"""
	return HttpResponseRedirect('/agile/')


 
def  tache_delete(request):
	"""
	Ici on va supprimer une  tache  grace a son id 
	"""

	if(request.method == "POST"):
		idToDelete = request.POST.get("pk")
		tacheToDelete = Tache.objects.get(pk = idToDelete )
		tacheToDelete.delete()
		print("La Tache a ete supprimer")
	return HttpResponseRedirect('/agile')


def tacheDelete(request , id):
	print(id)
	return HttpResponse('/agile')




class TacheDelete(DeleteView):
	"""
	Creation d une vue generic qui va permettre de supprimer
	des taches
	"""
	model = Tache
	template_name  = "tache_app/supprimer.html"
#	from_class = TacheForm
	success_url = reverse_lazy('tache')



class TacheCreate(CreateView):
	"""
	creation d' une vue genric pour ajouter une nouvelle tache
	"""
	model = Tache
	template_name = "tache_app/nouveau.html"
	fields = ('Etat' , 'Contenue' , 'TempsAConsacrer' , 'Deadline' , 'Priorite')
#	form_class = TacheForm
	success_url = reverse_lazy('tache')


class TacheUpdate(UpdateView):
	"""
	 Creation d une view afin de modifier les
	d une tache
	"""
	model = Tache
	template_name = "tache_app/edition.html"
	fields = ('Etat' , 'Contenue' , 'TempsAConsacrer' , 'Deadline' , 'Priorite')
	from_class = TacheForm
	success_url = reverse_lazy('tache')

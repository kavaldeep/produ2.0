from django.shortcuts import render
from django.http import HttpResponse
from tache_app.models import Tache , TacheTemps




def index(request):
    
    return render(request , 'finis/finis.html' ,  {"TachesFinis" : Tache.objects.filter(Etat = "Finis")} )


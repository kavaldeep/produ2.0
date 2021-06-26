from django.shortcuts import render
from tache_app.models import Tache
from tache_app.views import TacheCreate
from tache_app.forms import TacheFormAdd , TacheForm
from agile import dbUtilis
# Create your views here.
"""
Grace a cette view on va aller dans la base de donnees recuperer toutes les taches et les afficher
dans la page html

"""

def recup_tache(request): 	
	form  = TacheForm()
	tasks =dbUtilis.getTasks()
	return render(request , 'agile/agile.html' , {"listTache": tasks , "ajouter_tache" :form} )

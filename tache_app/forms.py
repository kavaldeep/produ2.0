from django import forms 
from .models import Tache

"""
les model forms son enregistrer ici	
"""
class TacheForm(forms.ModelForm):
    """
    Classe qui herite d une classe qui se trouve dans models.py --> Tache 
    Cette classe va servir a creer le formulaire 

    """
    class Meta:

        model = Tache 
        fields =  "__all__"



class TacheFormAdd(forms.ModelForm):

    class Meta:
        model = Tache
        fields = ["Etat" , "Contenue" ,  ]
     

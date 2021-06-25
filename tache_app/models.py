from django.db import models
from django.utils import timezone
import datetime 
from datetime import timedelta


class Tache(models.Model):
    """
    Tache Etait ----> Contiendra l etat de la tache : Encours , A faire , FINIT
    Date de Creation ----> La date quand la tache etait mise en ligne
    Contenue ----> Quelles est le contenue les instruction les chose a faire
    TempsAConsacrer ----> Combien de temps on va donner a la tache
    Deadline ----> pour quand est ce que c est a finir
    TempsConsacrer -----------> Le temps qu on a mis deja pour faire le projet
                Temps Restant = TempsAConsacer - TempsConsacrer
    on arrive pas a avoir un string dans django view donc on utlise les int
    PauseOuPlay----------> pause ou play la valeur 0 signfie pause
   TempsTemp-------------> variable pour enregistrer un temps temporaire pour
			   calculer le temps passer a travailer
    TempsClé -----------> contient les clés pour acceder au temps correspandant
			   dans la classe TacheTemps  merci
    """
    PrioriteChoice = [
            (  0   , "non important , non urgent"),
            ( 1 ," important ,  non urgent" ),
            (2,"non important , urgent"),
            ( 3,"import tant , urgent" ),
    ]
    EtatsChoice = [
            ("A faire" , "A faire"),
            ("En Cours" , "En Cours"),
            ("Finis" , "Finis"),
        ]



    Etat = models.CharField(max_length = 100 , choices=EtatsChoice)
    DateDeCreation = models.DateTimeField(null = False , blank = False , auto_now=True)
    Contenue = models.TextField()
    PauseouPlay = models.IntegerField(default = 0)
    TempsAConsacrer = models.DurationField(null= False )
    TempsConsacrer = models.DurationField(default=timedelta(0))
    Deadline = models.DateField(default = timezone.now)
    FinishDate = models.DateField(null = True , blank = True )
    TempsTemp = models.DateTimeField(auto_now=True)
    TempsCle  = models.TextField(default = "")
    Priorite = models.IntegerField( default = 0 , choices = PrioriteChoice)
    TempsRestant = models.DurationField(null = True )
    def __str__(self):
        chaine = "Etat:" + self.Etat + " Contenue:" + self.Contenue   
        return chaine



class TacheTemps(models.Model):
	"""Dans cette classe on va enregistrer les temps
           de travail debut et fin pour chaque tache
	  ca va contenir un string qu on pourra retirer apres
	"""
	TempsList = models.CharField(max_length = 100)

	def __str__(self):
		return self.TempsList



class TempsDeTravail(models.Model):
    """
    Dans cette CLasse on va enregistrer Les temps de travail effectuer 
    en fonction de La journee 
    """

    deltaTemps = models.DurationField(null = False)
    day = models.DateTimeField(null = False)

    def __str__(self):
        
        return self.day 

    def print():
        for elem in TempsDeTravail.objects.all():
            print(elem.day)

    def get(id):
        return TempsDeTravail.objects.get(pk = id)

    def dayData(day , mois):
        """
        Fonction pour retirer la data concernant un jour 
        day : Le jour  pendant le quel on veut la data 
        mois : Le mois correpandant 
        """
        liste = []
        [liste.append(0) for i in range(0,23)]
       
        for elem in TempsDeTravail.objects.all():
            if elem.day.day == day: 
                print(elem.day.day)
                liste[elem.day.hour] =  liste[elem.day.hour]  +  elem.deltaTemps.seconds/3600
        return liste

class FausseBase(models.Model):
	"""
	Fausse base pour faire des tests et afficher graphique
	"""
	TempsList = models.CharField(max_length = 100)

	def __str__(self):
		return self.TempsList


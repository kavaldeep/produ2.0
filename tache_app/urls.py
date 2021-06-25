"""Mettre les urls pour la tache app etc etc etc """
from django.urls import path 
from django.conf.urls import url
from . import views
from agile import dbUtilis
"""
	addToContenue l url avec add to contenue pour recevoir les post ajax
"""
urlpatterns = [
    path('tache_ajouter/' , dbUtilis.addTask , name='tache_ajouter' ),
	path('tache_delete/' , dbUtilis.deleteTask , name = 'tache_delete'),
	path('update_time/' , views.TimeUpdate , name = 'TimeUpdate'),
	path('updateTaskFinish/' ,  dbUtilis.updateFinish , name = 'updateTaskFinish'),
	path('updateTaskInProgress/' , dbUtilis.updateInProgress , name = "updateInProgress"),
	path('updateTaskToDo/' , dbUtilis.updateToDo, name = "updateToDo"),

	url(r'^TacheCreate$', views.TacheCreate.as_view(), name='TacheCreate'),		
	url(r'^TacheUpdate/(?P<pk>\d+)$', views.TacheUpdate.as_view(), name='TacheUpdate'),
	url(r'^TacheDelete/(?P<pk>\d+)$', views.TacheDelete.as_view(), name='TacheDelete'),	
	url(r'^ChangeToEnCours$', views.ChangeToEnCours, name='ChangeToEnCours'),
	url(r'^ChangeToAFaire$', views.ChangeToAFaire, name='ChangeToAFaire'),
	#url(r'^ChangeToFinis$', views.ChangeToFinis, name='ChangeToFinis'),
	#url(r'^addToContenue$', views.TimeUpdate, name='TimeUpdate'),
	
]

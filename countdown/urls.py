"""Mettre les urls pour countDown etc etc etc """
from django.urls import path
from . import views

urlpatterns = [
        path('' , views.countdown, name='countdown' ),
	#path('<int:pk>' , views.countdownWith , name='countdownTache')
        
        path('<int:pk>' , views.lancerCompteur , name='countdownTache')
        
]





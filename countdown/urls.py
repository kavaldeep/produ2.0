
############################COUNTDOWN
"""Mettre les urls pour countDown etc etc etc """
from django.urls import path
from . import views

urlpatterns = [
        #path('' , views.countdown, name='countdown' ),
	#path('<int:pk>' , views.countdownWith , name='countdownTache')
        path('' , views.launchCountDown , name = "countdown"),
        path('<int:pk>' , views.lancerCompteur , name='countdownTache'),
        path('getTime' , views.postGetTime , name = "postGetTime")
]




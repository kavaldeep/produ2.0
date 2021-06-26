"""Mettre les urls pour agile etc etc etc """
from django.urls import path
from . import views

urlpatterns = [
        path('' , views.recup_tache, name='tache' ),
]

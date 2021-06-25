"""Mettre les urls pour charts etc etc etc """
from django.urls import path
from . import views

urlpatterns = [
        #path('' , views.chartToday, name='chart' ),
        path('' , views.chartToday , name = 'chart'),
        path('chartMonth/' , views.chartMonth , name = 'chartMonth')
]

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('results/', views.results, name='results'),
    path('weather_results/', views.weather_results, name='weather_results')
]
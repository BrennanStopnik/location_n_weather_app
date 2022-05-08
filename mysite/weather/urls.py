from django.urls import path

from . import views

app_name = "weather"
urlpatterns = [
    path('', views.index, name="index"),
    path('results/', views.results, name="results"),
    path('contact/', views.contact, name="contact")
]
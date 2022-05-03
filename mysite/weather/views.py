from django.shortcuts import render
import requests as rqs
from django.http import HttpResponse
from .constants import * 
from .utils import *
from .forms import *

def index(request):
    return render(request, 'weather_stuff/index.html')


def search(request):
    if request.method == 'POST':
        form = NameForm(request.POST)

        if form.is_valid():
            address = form.cleaned_data['address']
            data = {
            'key': LOCATION_API_TOKEN,
            'q': address,
            'format': 'json'
            }
            try:
                response = rqs.get(LOCATION_API_URL, params=data).json()
            except Exception as e:
                raise e

            lat, lon = approx_coordinates(float(response[0]['lat']), float(response[0]['lon']))

            return HttpResponse(f"Lat = {lat} and Lon = {lon}")  
    else:
        return render(request, 'form.html')

def get_weather_info(lat, lon):
    WEATHER_API = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={WEATHER_API_TOKEN}"
    weather_data = rqs.get(WEATHER_API).json()

    result_dict = dict()
      
    current_temp = weather_data['main']['temp']
    result_dict['current_temp'] = kelvin_to_fahrenheit(current_temp)

    
    feels_like = weather_data['main']['feels_like']
    result_dict['feels_like'] = kelvin_to_fahrenheit(feels_like)


    temp_max = weather_data['main']['temp_max']
    result_dict['temp_max'] = kelvin_to_fahrenheit(temp_max)


    temp_min = weather_data['main']['temp_min']
    result_dict['temp_min'] = kelvin_to_fahrenheit(temp_min)
    
    
    return result_dict

def results(request):

    if request.method == 'POST':
        address = request.POST['address']
        data = {
        'key': LOCATION_API_TOKEN,
        'q': address,
        'format': 'json'
        }
        try:
            response = rqs.get(LOCATION_API_URL, params=data).json()
        except Exception as e:
            raise e

        lat, lon = approx_coordinates(float(response[0]['lat']), float(response[0]['lon']))
        res = get_weather_info(lat, lon)
        return render(request, 'weather_stuff/results.html', {'res': res})
       # return HttpResponse(f"Lat = {lat} and Lon = {lon}")  
    else:
        return render(request, 'index.html')






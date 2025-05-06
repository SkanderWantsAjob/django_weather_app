
import os
from django.shortcuts import render, HttpResponse
import requests
import datetime

OPENWEATHER_API_KEY = os.getenv('OPENWEATHER_API_KEY')


def home_view_render(request):
    if 'city' in request.POST:
        city= request.POST['city']
    else :
        city ="sousse"
        
    
    print(OPENWEATHER_API_KEY)
    url= f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}'
    PARAMS= {'units':'metric'}
    
    
    data= requests.get(url, PARAMS).json()
    print(data)
    
    description = data['weather'][0]['description']
    icon = data['weather'][0]['icon']
    temperature = data['main']['temp']
    date = datetime.date.today()
    return render(request, 'index.html', {'description': description, 'icon': icon, 'temperature': temperature, 'day': date})
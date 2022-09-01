from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm

def index(request):
    appid='ce353e843fb5c485d1458e8a13f32132'
    url="https://api.openweathermap.org/data/2.5/weather?q= {}&units=metric&appid="+appid

    if(request.method =='POST'):
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities=City.objects.all()
    all_cities=[]

    for city in cities:
        res=requests.get(url.format(city.name)).json()

        city_info={
            'city':city.name,
            'temp':res["main"]["temp"],
            'wind':res["wind"]["speed"],
            'icon':res["weather"][0]["icon"],
            'visibility':res["visibility"]
        }
        all_cities.append(city_info)

    context={'all_info':all_cities, 'form':form}

    return render(request, 'weath/index.html', context)

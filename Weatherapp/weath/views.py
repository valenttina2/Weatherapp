from django.shortcuts import render
import requests

def index(request):
    appid='ce353e843fb5c485d1458e8a13f32132'
    url="https://api.openweathermap.org/data/2.5/weather?q= {}&units=metric&appid="+appid
    city='Minsk'
    res=requests.get(url.format(city)).json()
    city_info={
        'city':city,
        'temp':res["main"]["temp"],
        'wind':res["wind"]["speed"],
        'icon':res["weather"][0]["icon"],
        'visibility':res["visibility"]
    }

    context={'info':city_info}

    return render(request, 'weath/index.html', context)

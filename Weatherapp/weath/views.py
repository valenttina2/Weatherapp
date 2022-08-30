from django.shortcuts import render
import requests

def index(request):
    appid='ce353e843fb5c485d1458e8a13f32132'
    url="https://api.openweathermap.org/data/2.5/weather?q= {}&units=metric&appid="+appid
    city='Minsk'
    res=requests.get(url.format(city))
    print(res.text)
    return render(request, 'weath/index.html')

from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm


#@crf_exempt
# Create your views here.
def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=a2290f5132b80143df242aa1fe7a093d'

    #city = 'Braga'
    #city_weather = requests.get(url.format(city)).json()
    cities = City.objects.all()
    
    weather_data = []
    #print(city_weather)

    if request.method == 'POST' :
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    for city in cities:

        a = requests.get(url.format(city)).json()

        city_weather = {
            'city' : city,
            'temperature' : a['main']['temp'],
            #'coord' : city_weather['lat']['lon'],
            'description' : a['weather'][0]['description'],
            'icon' : a['weather'][0]['icon']
        }

        weather_data.append(city_weather)

    context = {'weather_data' : weather_data, 'form' : form}
    return render(request, 'weather/index.html', context)
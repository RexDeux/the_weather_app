from django.shortcuts import render, redirect
import requests
from .models import City
from .forms import CityForm
from .gmaps import Google
import googlemaps

# @crf_exempt
# Create your views here.
class Weather():
    def index(request):
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=a2290f5132b80143df242aa1fe7a093d'

        city = 'Braga'
        #city_weather = requests.get(url.format(city)).json()
        cities = City.objects.all()

        weather_data = []
        message = ''
        message_class = ''
        err_msg = ''
        #print(city_weather)

        if request.method == 'POST':
            form = CityForm(request.POST)

            if form.is_valid():
                new_city = form.cleaned_data['name'].capitalize()
                existing_city_count = City.objects.filter(name=new_city).count()

                if existing_city_count == 0:
                    a = requests.get(url.format(city)).json()

                    if a['cod'] == 200:
                        form.save()
                    else:
                        err_msg = 'This city does not exist'
                else:
                    err_msg = 'City already exists in the database!'

            if err_msg:
                message = err_msg
                message_class = 'is-danger'
            else:
                message = 'City added'
                message_class = 'is-success'

        form = CityForm()

        for city in cities:

            a = requests.get(url.format(city)).json()

            city_weather = {
                'city': city.name,
                'temperature': a['main']['temp'],
                'temperature2': a['main']['feels_like'],
                'description': a['weather'][0]['description'],
                'icon': a['weather'][0]['icon'],
                'coordinate1': a['coord']['lon'],
                'coordinate2': a['coord']['lat'],
                'zone': a['sys']['country']

            }

            weather_data.append(city_weather)

        context = {'weather_data': weather_data, 'form': form,
                'message': message, 'message_class': message_class}

        return render(request, 'weather/index.html', context)


    def delete_city(request, city_name):
        City.objects.get(name=city_name).delete()

        return redirect('home')


    def delete_everything(request):
        cities = City.objects.all()
        for city in cities:
            City.objects.get(name=city).delete()
        return redirect('home')

    def maps(city_name):
        url = 'https://maps.googleapis.com/maps/api/js?key=AIzaSyBqm77Uo3KIONlVCMM20sNwjAnNnIhSmeo&callback=initMap'

        maps_data = []
        city = []
        a = requests.get(url.format(city)).json()
        geocode_result = gmaps.geocode('R. Dom Paio Mendes, 4700-424 Braga')
        reverse_geocode_result = gmaps.reverse_geocode((41.549935, -8.427262))

        maps_data.append()
                
        return render(request, 'weather/maps.html')
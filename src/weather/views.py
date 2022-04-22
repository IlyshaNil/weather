from django.shortcuts import render
from .forms import RegionForm
from .models import WeatherArchive
import requests
from dynaconf import settings as _settings
import time
from datetime import datetime


def main(request):
    return render(request, 'index.html', {'form': RegionForm()})


def forecast(request):

    def get_region_coord(request):
        geocoding_url = f'http://api.openweathermap.org/geo/1.0/direct?q={request.POST["region"]}&limit=1&appid={_settings.API_KEY}'
        return requests.get(geocoding_url).json()


    def unix_to_date(unix):
        return datetime.utcfromtimestamp(int(unix)).strftime('%Y-%m-%d')


    if request.method == 'POST':
        form = RegionForm(request.POST)
        
        lat_lon = get_region_coord(request)
        
        url = f'https://api.openweathermap.org/data/2.5/onecall?lat={lat_lon[0]["lat"]}&lon={lat_lon[0]["lon"]}&exclude=hourly,minutely,current,alert&appid={_settings.API_KEY}&units=metric'
        region_forecast = requests.get(url).json()

        requested_dates = []
        for day in region_forecast['daily']:
            if unix_to_date(day['dt']) >= request.POST['start_date'] and unix_to_date(day['dt']) <= request.POST['end_date']:
                day['dt'] = unix_to_date(day['dt'])
                requested_dates.append(day)



                
        return render(request, 'forecast.html', {'form': form, 
                                                'weather': requested_dates,
                                                'region': request.POST['region']})

    if request.method == 'GET':
        return render(request, 'forecast.html', {'form': RegionForm()})

  
def archive(request):
    if request.method == 'POST':
        date = datetime.datetime.strptime(request.POST['start_date'], '%Y-%m-%d')
        region = request.POST['region']

        year = WeatherArchive.objects.filter(date_from__year__gte=date.year, region__icontains=region)

        month = WeatherArchive.objects.filter(date_from__month__gte=date.month, region__icontains=region)

        start_week = date - datetime.timedelta(date.weekday())
        end_week = start_week + datetime.timedelta(7)
        weeek = WeatherArchive.objects.filter(created_at__range=[start_week, end_week], region__icontains=region)

    if request.method == 'GET':
        return render(request, 'forecast.html', {'form': RegionForm()})




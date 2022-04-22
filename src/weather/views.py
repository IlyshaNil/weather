from django.shortcuts import render
from .forms import ForecastForm, ArchiveForm
from .models import WeatherArchive
import requests
from dynaconf import settings as _settings
import time
from datetime import datetime
import datetime as dt


def main(request):
    return render(request, 'index.html', {'form': RegionForm()})


def forecast(request):

    def get_region_coord(request):
        geocoding_url = f'http://api.openweathermap.org/geo/1.0/direct?q={request.POST["region"]}&limit=1&appid={_settings.API_KEY}'
        return requests.get(geocoding_url).json()


    def unix_to_date(unix):
        return datetime.utcfromtimestamp(int(unix)).strftime('%Y-%m-%d')


    if request.method == 'POST':
        form = ForecastForm(request.POST)
        
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
        return render(request, 'forecast.html', {'form': ForecastForm()})

  
def archive(request):

    def average(qery):
        avr_day_temp = 0
        avr_ngt_temp = 0
        avr_humidity = 0
        for day in qery:
            avr_day_temp += day.day_temp
            avr_ngt_temp += day.night_temp
            avr_humidity += day.humidity
        avr_day_temp /= len(qery)
        avr_ngt_temp /= len(qery)
        avr_humidity /= len(qery)
        return round(avr_day_temp,2), round(avr_ngt_temp,2), round(avr_humidity,2) 

    if request.method == 'POST':
        form = ArchiveForm(request.POST)

        date = datetime.strptime(request.POST['start_date'], '%Y-%m-%d')
        region = request.POST['region']

        year = WeatherArchive.objects.filter(date__year__gte=date.year, region__icontains=region)
        data_year = average(year)

        month = WeatherArchive.objects.filter(date__month__gte=date.month, region__icontains=region)
        data_month = average(month)
    
        start_week = date - dt.timedelta(date.weekday())
        end_week = start_week + dt.timedelta(5)
        weeek = WeatherArchive.objects.filter(date__range=[start_week, end_week], region__icontains=region)
        data_week = average(weeek)

        return render(request, 'archive.html', {'form': ArchiveForm(), 
                                                    'year': data_year,
                                                    'month': data_month,
                                                    'week': data_week,
                                                    'region': region})


    if request.method == 'GET':
        return render(request, 'archive.html', {'form': ArchiveForm()})



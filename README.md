# Weather forecast

Simple django weather app using [OpenWeather](https://openweathermap.org/ "OpenWeather") api.  

In the "forecast" tab you can get information about the key weather parameters for the next 5 days. *(Restrictions on the forecast period are associated with API payment plan)* 

On the "archive" tab, you can get statistics on the average values ​​of key weather parameters in the selected region for a week/month/year. The selected day determines the periods for which statistics will be collected (week in which this day is, month in which this day is and etc.). Statistics data is stored in the database. *The database is initially empty. Solutions - request data from the api (no more than five days for the payment plan used), or use an automatic script that collects information on the required regions daily.*  

### Build with
1. Django
2. Django ORM  

### Installation  
###### Git  
Clone repo and run
 ```
 pipenv shell
 pipenv install
 python src/manage.py runserver
```  
Note: required:
1. Python 3.10
2. Pipenv
3. PostgreSQL 14 with DB "weather"
4. Secrets - at bottom  

###### Docker  
I'm not that familiar with docker - this was my first experience to make it easy to install and really hope that's enough.  
[Docker hub](https://hub.docker.com/repository/docker/ilyshanil/weather_web "docker")

### Testing
```
pipenv shell
cd src; pytest
```  

### Elapsed time  
2 days + 1 evening  
*It was realy difficult to choose api provider*  



###### Secrets 
You have to configure ***config/.secrets.yaml*** by this template:
```yaml
default:
  SECRET_KEY: '**********'
  DATABASE_URL: 'postgresql://user:password@host:5432/weather'
  API_KEY: ****************

docker:
  SECRET_KEY: "xxx"
  DATABASE_URL: "postgresql://postgres:postgres@db:5432/postgres"
  DJANGO_SUPERUSER_PASSWORD: 12345678
  DJANGO_SUPERUSER_EMAIL: hacharoky86@gmail.com
  DJANGO_SUPERUSER_USERNAME: admin
```  

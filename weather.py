from requests import get
from datetime import datetime, timedelta
from json import loads
from pprint import pprint

# api key
KEY = '9ba5ffb43e60e97639d8fd555fd731e2'

cities = open('city.list.json').readlines()

#get the city id based on user input
def get_city_id():
    with open('city.list.json') as f:
        data = [loads(line) for line in f]
    city = input('which is the closest city to the place you are travelling to?')
    city_id = False
    for item in data:
        if item['name'] == city:
            answer = input('Is this in '+item['country']+'?')
            if answer =='y':
             city_id = item['_id']
            break

    if not city_id:
        print('Sorry, that location is not avaliable!')
        exit()
    return city_id

def get_weather_data(city_id):
    weather_data = get('http://api.openweathermap.org/data/2.5/forecast?id={}&APPID={}'.format(city_id,KEY))
    return weather_data.json()

weather = get_weather_data('7839805')


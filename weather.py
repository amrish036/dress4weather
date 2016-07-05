from requests import get
from datetime import datetime, timedelta
from json import loads
from pprint import pprint

# api key
KEY = '9ba5ffb43e60e97639d8fd555fd731e2'

cities = open('city.list.json').readlines()

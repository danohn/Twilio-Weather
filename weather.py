import os
import requests
import json
from datetime import datetime
from tzlocal import get_localzone

weather_api_key = os.environ['OPEN_WEATHER_MAP_API_KEY']

def get_weather(_zip):
    
    url = f'https://api.openweathermap.org/data/2.5/weather?zip={_zip},au&units=metric&appid={weather_api_key}'
    print(url)
    resp = requests.get(url).json()
    weather = {
        'weather_description': resp['weather'][0]['description'],
        'weather_temp': resp['main']['temp'],
        'weather_feels_like': resp['main']['feels_like'],
        'weather_feels_min': resp['main']['temp_min'],
        'weather_feels_max': resp['main']['temp_max'],
        'weather_wind_speed': resp['wind']['speed'],
        'weather_sunset_time': datetime.fromtimestamp(int(resp['sys']['sunset']), get_localzone()).strftime('%H:%M'),
        'location_name': resp['name']
        }
    
    annoucement = f"""
    Today\'s weather for {weather['location_name']} is {weather['weather_description']}.
    It\'s {weather['weather_temp']} degrees but feels like {weather['weather_feels_like']} degrees.
    The coldest temperature today will be {weather['weather_feels_min']} and the hottest temperature will be {weather['weather_feels_max']}.
    The windspeed is currently {weather['weather_wind_speed']} meters per second.
    Today's sunset will be at {weather['weather_sunset_time']}.
    """
    
    
    return annoucement

if __name__ == '__main__':
    my_weather = get_weather()
    print(my_weather)
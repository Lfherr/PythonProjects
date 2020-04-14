"""
TODO
1. Reads requested location from command line
2. Downloads weather data from OpenWeatherMap.org
3. Convert string from json to Python
4. Prints weather for today and next two days
"""
import json
import requests
import sys


APPID = '66924d22bfe66aa7eeea40f0f1595c32' #API Key
command_line = input('Enter city and state ')
print(command_line)
#1. Reads Command line info
if len(command_line)<2:               #Checks that enough values are passed into program or it quits
    print('Usage: getOpenWeather.py city_name, 2-letter_country_code')
    sys.exit()

else:
    location = ''.join(command_line)    #Turns value into Python string


    #2. Get data from OpenWeatherMap.org
    url = 'https://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3&appid=%s' %(location, APPID)

    response = requests.get(url)        #pulls in data from the given url
    response.raise_for_status()         #checks for errors.


    #3. Convert from json to Python
    weather_data = json.loads(response.text) #Json to Python variable

    #4. Prints weather descriptions
    w = weather_data['list']
    print('Current weather in %s.' %(location))
    print(w[0]['weather'][0]['main'], '-', w[0]['weather'[0]]['description'])
    print()
    print('Tomorrow:')
    print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
    print()
    print('Day after tomorrow:')
    print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])



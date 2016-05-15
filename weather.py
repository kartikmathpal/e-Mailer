import requests
def get_weather_forecast():
    url = 'http://api.openweathermap.org/data/2.5/find?q=Bangalore&units=metric&appid=13093b1b0a356c3b029cce493525824d'
    weather_request = requests.get(url) #returns request object 
    weather_json = weather_request.json() #returns data in json format
    #print(weather_json)
    description = weather_json['list'][0]['weather'][0]['description']
    #print(description)
    temp_min = weather_json['list'][0]['main']['temp_min']
    #print(temp_min)
    temp_max = weather_json['list'][0]['main']['temp_max']
    #print(temp_max)

    forecast = 'Today\'s forecast is:\n ' + description + ' with a high of ' + str(temp_max) +'C  and a low of ' + str(temp_min) + 'C'
    #print(forecast)
    return forecast

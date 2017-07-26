from urllib2 import urlopen
import json
import ctypes
import time

#request weather data

url = 'http://api.openweathermap.org/data/2.5/weather?zip=%s,us&APPID=%s'
zip_code= '90024'
API_KEY = 'c85d528ba3cdbcb4945277f6fb06f4de'

    #loop every hour
while API_KEY == 'c85d528ba3cdbcb4945277f6fb06f4de':
    response=urlopen(url%(zip_code, API_KEY))
    json_string = response.read()
    parsed_json = json.loads(json_string)
    ID= parsed_json.get('weather')[0].get('id')

#map parsed response to a background image

    if ID < 233: #thunderstrom= 200-232
        image_path = "C:\Users\kpet5\src\BackgroundByWeather\BackgroundPictures\thunderstorm.jpg"
    elif 299 < ID < 322: #drizzle= 300-321
        image_path = "C:\Users\kpet5\src\BackgroundByWeather\BackgroundPictures\Drizzle.jpg"
    elif  499 < ID < 532: #rain=500-531
        image_path = "C:\Users\kpet5\src\BackgroundByWeather\BackgroundPictures\Rain.jpg"
    elif 699 < ID < 623: #snow=600-622
        image_path = "C:\Users\kpet5\src\BackgroundByWeather\BackgroundPictures\Snow.jpg"
    elif 700 < ID < 782: #atm=701-781
        image_path = "C:\Users\kpet5\src\BackgroundByWeather\BackgroundPictures\ATM Italy.jpg"
    elif ID == 800: #clear=800
        image_path = "C:\Users\kpet5\src\BackgroundByWeather\BackgroundPictures\Clear landsEndForest.jpg"
    elif 800 < ID < 805: #clouds=801-804
        image_path = "C:\Users\kpet5\src\BackgroundByWeather\BackgroundPictures\Clouds Colosseum.jpg"
    elif 899 < ID < 907: #extreme=900-906
        image_path = "C:\Users\kpet5\src\BackgroundByWeather\BackgroundPictures\Xtreme landsendlabyrinth.jpg"
    elif ID > 950: #wind=951-962
        image_path = "C:\Users\kpet5\src\BackgroundByWeather\BackgroundPictures\Wind MiamiBeach2.jpg"
#set background image
    SPI_SETDESKWALLPAPER = 20 
    ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, image_path, 3)
    time.sleep(3600)


#use startup to make it run in the background, while loop repeats



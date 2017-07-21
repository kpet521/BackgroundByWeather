import urllib2
import json
import re
import ctypes
import os

#request weather data

url = 'http://api.openweathermap.org/data/2.5/weather?zip=%s,us&APPID=%s'
zip_code= '90024'
API_KEY = 'c85d528ba3cdbcb4945277f6fb06f4de'
response=urllib2.urlopen(url%(zip_code, API_KEY))
json_string = response.read()
    # if ^ is actually a string, why did I have to turn it into a string in 2 lines?
parsed_json = json.loads(json_string)
array = str(parsed_json.get('weather'))
print array[15] #this gives you "e" woooo

#how do I access the weather ID and not just the whole weather...
#weather_ID = re.findall(r'2|3|4|5|6|7|8|9', weather)
#print weather_ID

#map parsed response to a background image

#if weather_ID == '8':
    #image_path = "C:\Users\kpet5\src\BackgroundByWeather\BackgroundPictures\MiamiBeach2.jpg"
    #SPI_SETDESKWALLPAPER = 20 
    #ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, image_path, 3)
#else:
    #print('darn')


#So the response you got back is formatted
#as "json" which stands for JavaScript object
#notation and is by far the most popular and
#easiest way to serialize data
#(data serialization is the process of taking
#data and translating it into something that
#can be sent to and understood by other programs)
#Json is basically a big key / value mapping
#The keys are all strings (strings are what
#programmers call plain text) and the values
#can either be strings, numbers, or more json
#(another key / value mapping)
#Specifically how you access the data in the json
#response will depend on what you used to parse it,
#but it will probably end up looking like
#Response.get("weather").get("code")
#So "weather" is a key and get("weather") returns
#the value mapped to by the key, which in the example
#is another json object
#When I checked out that api I remember seeing in the
#response definition some kind of weather code. I think
#that would be the best thing to use to determine what picture to show

#windows api to set the image
    #drive = "C:\Users\kpet5\Pictures"
    #folder = "Saved Pictures"
    #image = "Colosseum.jpg"
    #image_path = os.path.join(drive, folder, image)
#for id=8XX



#use startup to make it run in the background

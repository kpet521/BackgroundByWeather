import urllib2
import json
import ctypes
import os

#request weather data

url = 'http://api.openweathermap.org/data/2.5/weather?zip=%s,us&APPID=%s'
zip_code= 90024
API_KEY = 'c85d528ba3cdbcb4945277f6fb06f4de'
response=urllib2.urlopen(url%(zip_code, API_KEY))
json_string = response.read()
parsed_json = json.loads(json_string)
print(parsed_json.get('weather'))
#map parsed response to a background image

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
image_path = "C:\Users\kpet5\Pictures\Saved Pictures\Crepes.jpg"
SPI_SETDESKWALLPAPER = 20 
ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, image_path, 3) 


#use startup to make it run in the background

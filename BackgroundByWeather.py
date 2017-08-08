from urllib2 import urlopen
import json
import ctypes

#request weather data

url = 'http://api.openweathermap.org/data/2.5/weather?zip=%s,us&APPID=%s'
zip_code= '90024'
API_KEY = 'c85d528ba3cdbcb4945277f6fb06f4de'

response = urlopen(url%(zip_code, API_KEY))
json_string = response.read()
parsed_json = json.loads(json_string)
ID= parsed_json.get('weather')[0].get('id')

#map parsed response to a background image

weather={2:'thunderstorm',3:'drizzle',5:'rain',6:'snow',7:'atm',8:'mostly clear',9:'extreme'}
weather=weather[ID/100]
folder = 'C:\Users\kpet5\src\BackgroundByWeather\BackgroundPictures\%s.jpg'
image_path = folder%(weather)
    
#set background image
SPI_SETDESKWALLPAPER = 20 
ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, image_path, 3)
  



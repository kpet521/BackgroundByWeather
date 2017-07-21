import urllib2
import json
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



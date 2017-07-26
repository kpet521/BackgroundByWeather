import urllib2
import json
#request weather data

url = 'http://api.openweathermap.org/data/2.5/weather?zip=%s,us&APPID=%s'
zip_code= '90024'
API_KEY = 'c85d528ba3cdbcb4945277f6fb06f4de'
response=urllib2.urlopen(url%(zip_code, API_KEY))
json_string = response.read()
parsed_json = json.loads(json_string)
ID= parsed_json.get('weather')[0].get('id')
print ID



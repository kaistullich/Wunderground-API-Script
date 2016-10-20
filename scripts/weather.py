import urllib2
import json

print ('hello my name is Kai')
wunderground_url = urllib2.urlopen('http://api.wunderground.com/api/ed52388436c43bbe/geolookup/conditions/q/CA/Morgan_Hill.json')

json_string = wunderground_url.read()

parsed_json = json.loads(json_string)

location = parsed_json['location']['city']

temp_f = parsed_json['current_observation']['temp_f']

print ("Current temperature in %s is: %s" % (location, temp_f))

wunderground_url.close()
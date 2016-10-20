import urllib2
import json

user_state = raw_input("Please enter the State's abbreviation (i.e. CA, NV, etc): ")

user_state_upper = user_state.upper()

user_city = raw_input('Please enter the City of the State you are inquiring about: ')

user_city_replace = user_city.replace(" ", "_")

user_replace_title = user_city_replace.title()


wunderground_url = urllib2.urlopen('http://api.wunderground.com/api/ed52388436c43bbe/geolookup/conditions/q/CA/Morgan_Hill.json')

json_string = wunderground_url.read()

parsed_json = json.loads(json_string)

location = parsed_json['location']['city']

temp_f = parsed_json['current_observation']['temp_f']

print ("Current temperature in %s is: %s" % (location, temp_f))

wunderground_url.close()


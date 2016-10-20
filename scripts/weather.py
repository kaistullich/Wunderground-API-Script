# -*- coding: utf-8 -*-

import urllib2
import json
import sys  

reload(sys)  
sys.setdefaultencoding('utf8')

choice = ""

while True:
    # Allows user to set the State in which they want to search
    user_state = raw_input("\nPlease enter the State's abbreviation (i.e. CA, NV, etc): ")
    # This will auto capitalize the abbreviation, if user did not do so already (i.e. ca = CA)
    user_state_upper = user_state.upper()



    # Allows the user to specify which City they want to search from within the State
    user_city = raw_input('Please enter the City of the State you are inquiring about: ')
    # This variable will replace any white space for Cities with 2 words, 
    # and add an Underscore (i.e. San Francisco = San_Francisco)
    user_city_replace = user_city.replace(" ", "_")
    # This variable will Auto-Capitalize the city (i.e. san francisco = San_Francisco)
    user_replace_title = user_city_replace.title()



    # URL that leads to Wundergound weather
    wunderground_url = urllib2.urlopen('http://api.wunderground.com/api/ed52388436c43bbe/geolookup/conditions/q/%s/%s.json' % (user_state,user_replace_title))

    json_string = wunderground_url.read()

    parsed_json = json.loads(json_string)

    location = parsed_json['location']['city']

    temp_f = parsed_json['current_observation']['temp_f']

    print ("\nThe current temperature in %s is: %s °F" % (location, temp_f))
    
    # User is able to choose wether they want to EXIT or continue the program
    user_choice = raw_input('\nWould you like to EXIT the program? (y/n): ')
    if user_choice == "n":
        pass
    #This will EXIT the program
    if user_choice == "y":
        break
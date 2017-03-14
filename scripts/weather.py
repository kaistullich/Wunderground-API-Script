import requests
import json

while True:
    user_state = input("\nPlease enter the State's abbreviation (i.e. CA, NV, etc): ").upper()
    user_city = input('Please enter the City of the State you are inquiring about: ').replace(" ", "_").title()
    wunderground_url = requests.get('http://api.wunderground.com/api/ed52388436c43bbe/geolookup/conditions/q/{st}/ \
                                    {st_r}.json'.format(st=user_state, st_r=user_city))

    json_string = wunderground_url.text
    parsed_json = json.loads(json_string)
    location = parsed_json['location']['city']
    temp_f = parsed_json['current_observation']['temp_f']

    print("\nThe current temperature in {loc} is: {deg} °F".format(loc=location, deg=temp_f))

    while True:
        accepted_no_answer = ['no', 'n']
        accepted_yes_answer = ['yes', 'y']
        user_choice = input('\nWould you like to EXIT the program? (y/n): ')
        if user_choice in accepted_no_answer:
            break
        elif user_choice in accepted_yes_answer:
            break
        else:
            print('Please only answer either yes or no')

    if user_choice in accepted_yes_answer:
        break

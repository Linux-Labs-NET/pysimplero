import requests
import json
from secrets import *

class Pysimplero:
    """Python module to interact with the simplero api.
       initialise with api_key and user_agent

    """
    def __init__(self, api_key, user_agent):
        """Initialise get api key and user agent """
        self.api_key = api_key
        self.user_agent = user_agent
        
        
    def get_lists(self):
        """Get all lists from simplero"""
        headers = {'User-Agent': user_agent,}

        response = requests.get('https://simplero.com/api/v1/lists.json', headers=headers, auth=(api_key, ''))
        parsed = json.loads(response.content)
        # prettyparsed = json.dumps(parsed, indent=4, sort_keys=True)
        # print(prettyparsed)
        for i in range(len(parsed)):
            list_ids = parsed[i]
            print("{\"ID\": ", list_ids['id'], ", \"name\":  ","\"" , list_ids['name'],"\" }")

        return response

    def add_subscriber(self, list_id, data):
        """To add or update something, include the JSON data with a =Content-Type= header
        Email and list_id required"""
        headers = {'User-Agent': user_agent,}
        self.data = data
        self.list_id = list_id
        url = "https://simplero.com/api/v1/lists/" + str(list_id) + "/subscribe.json"
        subscribe = requests.post(url, headers=headers, data=data, auth=(api_key, ''))
        parsed = json.loads(subscribe.content)
        prettyparsed = json.dumps(parsed, indent=4, sort_keys=True)
        print(prettyparsed)
        return subscribe 

    

              
p = Pysimplero(api_key, user_agent)
lists = p.get_lists()
# data = { "first_name": "Pysimplero AKROBAT", "email": "lando@akrobatonline.dk" }
# newsub = p.add_subscriber(list_id='93848', data=data)

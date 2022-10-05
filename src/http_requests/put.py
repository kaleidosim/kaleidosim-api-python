import requests
import json
from user_token import UserToken
from pathlib import Path
from .retry_wrapper import proccess_response

# loading config.json
path = str(Path.cwd())

with open(path + "/config/config.json", 'r') as file:
    data = file.read()


json_config = json.loads(data)


"""
   PUT http request to api-service endpoint 
"""


async def put(route, data, params=""):
    retryCount = 0
    completed = False
    response = None

    url = json_config['apiBaseURL']+route + params
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer " + UserToken.value,
    }

    while not completed:
        try:
            retryCount += 1
            print("retry count: " + str(retryCount))
            response = requests.put(
                url, data=json.dumps(data), headers=headers)
            completed = await proccess_response(response.json(), completed, retryCount, None)
        except requests.exceptions.RequestException as error:
            print(error)
            print("Error retrying", error)
            completed = await proccess_response(error, completed, retryCount, error)

    return response.json()

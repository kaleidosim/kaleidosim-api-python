import requests
import json
from user_token import UserToken
from .retry_wrapper import proccess_response
from pathlib import Path

# loading config.json file
path = str(Path.cwd())

with open(path + "/config/config.json", 'r') as file:
    data = file.read()


json_config = json.loads(data)

"""
   DELETE request to api-service 
"""


async def delete(route, params=""):

    retryCount = 0
    completed = False
    response = None

    url = json_config['apiBaseURL']+route + params
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer " + UserToken.value
    }
    while not completed:
        try:
            retryCount += 1
            print("retry count: " + str(retryCount))
            response = requests.delete(url, headers=headers)
            completed = await proccess_response(response.json(), completed, retryCount, None)
        except requests.exceptions.RequestException as error:
            print(error)
            print("Error retrying", error)
            completed = await proccess_response(error, completed, retryCount, error)

    return response.json()

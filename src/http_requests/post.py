import requests
import json
from pathlib import Path
from .retry_wrapper import proccess_response
from user_token import UserToken


# loading config.json
path = str(Path.cwd())

with open(path + "/config/config.json", 'r') as file:
    data = file.read()


json_config = json.loads(data)


# async def post(route, data, params=""):
#     result = await retry_wrapper(postRequest(route, data, params))

#     return result


"""
   POST request to api-service 
"""

# @retry(stop_max_attempt_number=100, wait_fixed=1000, retry_on_exception=retry_google_new_proccess, wrap_exception=True)


async def post(route, data, params=""):
    retryCount = 0
    completed = False
    response = None

    url = json_config['apiBaseURL']+route + params

    headers = {
        "accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer " + UserToken.value,
        "Origin": "0.0.0.0"
    }

    while not completed:
        try:
            retryCount += 1
            print("retry count: " + str(retryCount))
            response = requests.post(url, data=data, headers=headers)
            completed = await proccess_response(response.json(), completed, retryCount, None)
        except requests.exceptions.RequestException as error:
            print(error)
            print("Error retrying", error)
            completed = await proccess_response(error, completed, retryCount, error)

    return response.json()

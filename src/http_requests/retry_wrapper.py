import time

MAX_RETRIES = 20
RETRAY_DELAY_MS = 1
newProcessStartedStatus = "This request caused a new process to be started for your application"


async def proccess_response(response, completed, retryCount, error):
    # check if response has status code first
    if("error" in response):
        completed = check_response_service_400(response["error"])
    completed = await process_completed_state(response, completed, retryCount, error)
    return completed


async def process_completed_state(response, completed, retryCount, error):
    if(response["success"] == True):
        return True
    elif (response["success"] == False):
        print("Request to api with failures, please check your code")
        print(response)
        return True

    if(completed == False):
        if(retryCount <= MAX_RETRIES):
            time.sleep(RETRAY_DELAY_MS)
            print("Google starting new process, retrying this comms request")
        else:
            completed = True
            print("Retrying request total failure after retries")
        if (error != None):
            raise error

    return completed


def check_response_service_400(response):
    completed = True
    if(response["statusCode"] == 404):
        completed = False
    elif (response["statusCode"] == 400):
        response_text = response["message"]

        if (response_text == newProcessStartedStatus):
            completed = False
    return completed

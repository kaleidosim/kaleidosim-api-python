from api_requests.auth.login import login
from api_requests.projects.list import list_projects
from api_requests.projects.create import create_project
from api_requests.projects.count import count_projects
from api_requests.cases.create import create_case
from api_requests.files.upload_input_file import upload_input_file
from api_requests.files.upload import upload_file
from api_requests.run_case.run import run
from api_requests.run_case.get_case_status import get_case_status
from data.case_data import input_data
from download_case_files import download_case_files
from data.case_data import case_data, project_data
import json
import time
import os
from user_token import UserToken
import fire


directory_path = os.getcwd()
project_path = directory_path.replace("/src", "")
input_file_path = project_path + "/test_files/quickcase1.zip"

"""
API Example to run a single case
"""

async def run_example():

    print("Init")

    local_token = login()

    UserToken.value = local_token

    # response = list_projects()
    # print(response)
    project_data_req = json.dumps(project_data)

    # creating a project
    project_id = await create_project(project_data_req)

    # creating an input file
    input_file = await upload_input_file(input_data)

    # uploading input file to g storage
    upload_file(input_file['data']['resumableUploadUrl'], input_file_path)

    case_data['inputFileId'] = input_file['data']['fileId']

    # setting up case_data for creating a case
    case_data_req = json.dumps(case_data)

    # creating a case
    case_id = await create_case(project_id, case_data_req)

    time.sleep(15)
    # running the created case
    await run(case_id)

    # getting current status for the case
    current_status = await get_case_status(case_id)

    status = current_status['data']['caseStatus']

    # waiting case to be completed
    while(status != "Completed"):
        time.sleep(5)
        current_status = await get_case_status(case_id)
        status = current_status['data']['caseStatus']
        print(status)

    # when case is completed, download the generated files
    await download_case_files(case_id)

    print("Done")


if __name__ == '__main__':
    fire.Fire()

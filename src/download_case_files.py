from data.case_data import case_data, project_data
from api_requests.run_case.get_case_status import get_case_status
from api_requests.run_case.run import run

from api_requests.case_files.download_files import download_files_locally
from api_requests.case_files.get_case_files_by_case_id import get_case_files
import json


async def download_case_files(case_id):

    case_files = await get_case_files(case_id)

    case_files_id = []

    for case_file in case_files['data']:
        case_files_id.append(case_file['_id'])

    res = await download_files_locally(case_id, case_files_id)

    return res

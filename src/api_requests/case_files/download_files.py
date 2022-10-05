from http_requests.post import post
import requests
import shutil
import json
from pathlib import Path

path = str(Path.cwd().parent)
"""
    downloading files and saving to local folder (output_folder)
    response
        {
            "success": true,
            "message": "string",
            "data": [
                {
                "caseFileId": "string",
                "fileName": "string",
                "downloadURL": "string",
                "downloadURLExpiresOn": "string"
                }
            ]
        }

"""


async def download_files_locally(case_id, case_files):

    data = json.dumps(case_files)

    response = await post("/files/getDownloadSignedUrl/byCaseFilesId/", data, case_id)

    case_files_download = response['data']

    # looping each file and starting to download
    for case_file in case_files_download:
        filename = case_file['fileName']
        url = case_file['downloadURL']

        with requests.get(url, stream=True) as read:
            read.raise_for_status()
            # this is the place where files are downloaded
            saved = path + '/src/output_folder/' + filename
            with open(saved, 'wb') as file_save:
                # writing files to file
                shutil.copyfileobj(read.raw, file_save)

    return True

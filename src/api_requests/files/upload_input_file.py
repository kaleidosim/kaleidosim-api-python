
from http_requests.post import post

import json
"""
    calling upload signed url 
    returns 
        {
            "success": true,
            "message": "string",
            "data": {
                "fileId": "string",
                "resumableUploadUrl": "string"
            }
        }
"""
# reads value from (/data/case_data.py)


def upload_input_file(input_data):

    input_file = json.dumps(input_data)

    response = post("/files/getUploadSignedUrl", input_file)

    return response

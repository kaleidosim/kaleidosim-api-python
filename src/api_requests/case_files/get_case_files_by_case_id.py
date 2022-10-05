
from http_requests.get import get
import json

"""
    calling case files endpoint
    response
        {
            "success": true,
            "message": "string",
            "data": [
                {
                "projectId": "string",
                "caseId": "string",
                "_id": "string",
                "fileName": "string",
                "fileExt": "string",
                "filePath": "string",
                "fileSize": "string",
                "caseFileName": "string",
                "createdOn": "string"
                }
            ]
        }
"""

# requires a valid case_id


async def get_case_files(case_id):
    response = await get("/files/", case_id)
    return response

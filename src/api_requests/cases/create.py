
from http_requests.post import post
"""
    calling create endpoint
    response
    {
        "success": true,
        "message": "string",
        "data": {
            "caseId": "string"
        }
    }       
"""
# requires a valid projec_id
# data is loaded from (/data/case_data.py)


async def create_case(project_id, data):

    response = await post("/cases/create/", data, project_id)
    print(response)
    return response['data']['caseId']

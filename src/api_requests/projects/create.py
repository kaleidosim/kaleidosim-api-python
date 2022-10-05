
from http_requests.post import post
"""
    calling Post create project
    response
    {
        "success": true,
        "message": "string",
        "data": {
            "projectId": "string"
            }
    }
"""
# data should look like project_data variable in (/data/case_data.py)


async def create_project(data):

    response = await post("/projects/create", data)
    return response['data']['projectId']

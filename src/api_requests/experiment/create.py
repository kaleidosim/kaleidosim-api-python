
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
def create_experiment_project(data):
    
    response = post("/projects/experiment/create",data)
    return response['data']['projectId']
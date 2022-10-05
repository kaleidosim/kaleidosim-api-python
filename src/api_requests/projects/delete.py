
from http_requests.delete import delete

"""
    calling delete project endpoint
    response
    {
        "success": true,
        "message": "string"
    }    
"""
#requires a valid project_id
def delete_project(project_id):
    response = delete("/projects/delete/",project_id)
    return response
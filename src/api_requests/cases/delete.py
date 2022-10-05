
from http_requests.delete import delete

"""
    calling delete case endpoint
    {
     "success": true,
     "message": "string"
    }
"""
# requires a valid case_id
def delete_case(case_id):
    response = delete("/cases/delete/",case_id)
    return response
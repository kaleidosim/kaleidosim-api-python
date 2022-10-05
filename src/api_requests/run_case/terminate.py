
from http_requests.post import post

"""
    calling terminateCase endpoint
    response
    {
        "success": true,
        "message": "string"
    }
"""

# requires a valid case_id
def terminate_case(case_id):
    
    response = post("/caseRun/terminateCase/",{},case_id)
    return response
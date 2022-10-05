
from http_requests.post import post


"""
    calling abort endpoint
    response looks like this
    {
      "success": true,
      "message": "string"
    }
    
"""
#requires a valid case_id
def abort_case(case_id):
    
    response = post("/caseRun/abortCase/",{},case_id)    
    # accesing values like this response['success']
    return response
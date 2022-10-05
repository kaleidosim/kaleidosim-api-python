
from http_requests.get import get
"""
    calling getLastLogLines
    
    response looks like this
    {
        "success": true,
        "timeStep": "string"
    }
"""
#requires a valid case_id
def get_last_log_lines(case_id):
    
    response = get("/caseRun/lastLogLines/",case_id)
    return response
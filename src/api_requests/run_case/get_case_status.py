
from http_requests.get import get

"""
    calling caseStatus endpoint
    response looks like this
    {
      "success": true,
      "message":"string",
      "data":{
          "caseStatus":"string"
      }
    }
    
"""
# requires a valid case_id


async def get_case_status(case_id):
    response = await get("/caseRun/caseStatus/", case_id)
    return response

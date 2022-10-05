
from http_requests.post import post

"""
    calling runCase endpoint
    {
        "success": true,
        "message": "string"
    }
"""

# requires a valid case_id


async def run(case_id):

    response = await post("/caseRun/runCase/", {}, case_id)
    print(response)
    return response

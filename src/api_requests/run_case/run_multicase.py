
from http_requests.post import post

"""
    calling runMultiCase endpoint
    response
    {
        "success": true,
        "message": "string"
    }
"""

# requires an array of cases_id
# ['case_id_1','case_id_2']


def run_multicase(cases):

    response = post("/caseRun/runMultiCases/", cases, "")
    return response


from http_requests.get import get

"""
    calls cases/list endpoint
        {
            "success": true,
            "message": "string",
            "data": [
                {
                "caseId": "string",
                "name": "string",
                "caseStatus": "string",
                "machine": {
                    "numCPU": 0,
                    "vmMemory": 0
                },
                "software": {
                    "simulationSoftware": "string",
                    "version": "string",
                    "solverName": "string",
                    "decomposeParDict": "string",
                    "runScript": "string",
                    "parallel": true
                },
                "caseInputFile": {
                    "fileId": "string",
                    "name": "string",
                    "sizeInBytes": 0
                }
                }
            ]
        }
"""

# requires a valid project_id
def list_cases(project_id):
    response = get("/cases/list/",project_id)
    return response['data']
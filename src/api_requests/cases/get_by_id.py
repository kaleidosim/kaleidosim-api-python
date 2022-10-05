
from http_requests.get import get
"""
    calling caseInfo endpoint
    response
        {
            "success": true,
            "message": "string",
            "data": 
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
        }
"""
# requires a valid case_id
def get_by_id(case_id):
    response = get("/cases/caseInfo/",case_id)
    return response

from http_requests.get import get
"""
    calling get project endpoint
    response
        {
        "_id": "string",
        "name": "string",
        "nameLower": "string",
        "version": "string",
        "simulationSoftware": "string",  
        "userId": "string",
        "cases": [
                {
                    "_id": "string",
                    "name": "string",
                    "caseStatus": "string",
                    "parallel": true,
                    "runScript": "string",
                    "cloudProvider": "string",
                    "solverName": "string",
                    "decomposeParDict": "string",          
                    "inputFiles": [
                        {
                            "_id": "string",
                            "fileId": "string"
                        }
                    ],
                    "machineType": "string"
                }
                ],
        }
"""
#requires a valid project_id
def get_by_id(project_id):
    response = get("/projects/getProjectInfo/",project_id)
    return response
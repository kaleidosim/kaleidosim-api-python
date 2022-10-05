
from http_requests.get import get
"""
    calling project list endpoint
"""
# returns the projects for the given user (useing token)
def list_projects():
    response = get("/projects/list")
    return response
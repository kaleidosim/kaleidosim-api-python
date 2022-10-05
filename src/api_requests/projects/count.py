
from http_requests.get import get
"""
    calling count endpoint
"""
#returns the number of project for the logged user
def count_projects():
    response = get("/projects/count")
    return response
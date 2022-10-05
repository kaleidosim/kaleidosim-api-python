#!/usr/bin/env python3

import requests
import logging

"""
   Calling /ping endpoint example 
"""
def ping():
    print('GET /ping request')
    response = requests.get('https://api.kaleidosim.com/ping')
    print(response.status_code)
    # use response.json() to get the information required
    print(response.json())
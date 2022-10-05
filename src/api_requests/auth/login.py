import requests
import json
from pathlib import Path

path = str(Path.cwd())

with open(path + "/config/config.json",'r') as file:
    data= file.read()


json_config = json.loads(data)

"""
    calling login endpoint
    returns the token that is used for further endpoints
"""
def login():
  url = json_config['apiBaseURL'] + "/auth/login"
  body = { "email": json_config['user']['email'], "password": json_config['user']['password'], "twoFactorAuthenticationCode": "123456" }
  headers = {    
      "accept": "application/json",
      "Content-Type": "application/json",    
  }

  response = requests.post(url, data=json.dumps(body),headers=headers)
  json_res= response.json()
  print("Login success!🚀")
  print("Token generated: ", json_res['token'])
  return json_res['token']




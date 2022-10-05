"""
   here the token value is set and then reused on other files 
"""

class UserToken:
   value=""
      
def set_token(token):
   Token.value=token
   
def get_token():
   return Token.value
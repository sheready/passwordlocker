import pyperclip
import random
import string
class Users:
   
   user_list = []    
   
        
        
   def __init__(self,full_name,user_name,password):
        self.user_name = user_name
        self.full_name = full_name
        self.password = password
        
   
   def save_user(self):
        Users.user_list.append(self)
  
   
   def delete_user(self):
       Users.user_list.remove(self)
    
   
class Credentials:
    credential_list = []
    user_credential_list = []

    @classmethod
    def check_user(cls,user_name,password):
        current_user = ''
        for user in Users.user_list:
            if (user.user_name == user_name and user.password == password):
                 return True
            return False
    
    @classmethod
    def display_users(cls):
        return cls.user_list
    
                
          
    def __init__(self,user_namez,site_name,passwordz):
        self.user_namez = user_namez
        self.site_name = site_name
        self.passwordz = passwordz
    
    def save_credential(self):
        Credentials.credential_list.append(self)
    
    def delete_credentials(self):
        Credentials.credential_list.remove(self)

    @classmethod
    def rand_pass(cls,size):
        generate_pass = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(size)])
        return generate_pass
    
   
    @classmethod
    def display_credentials(cls):
        return cls.credential_list
    
    



      
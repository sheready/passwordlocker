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
                current_user = user_name
                return current_user 
          
    def __init__(self,user_name,site_name,password):
        self.user_name = user_name
        self.site_name = site_name
        self.password = password
    
    def save_credentials(self):
        Credentials.credential_list.append(self)
    
    def delete_credentials(self):
        Credentials.credential_list.remove(self)

    @classmethod
    def rand_pass(cls,size):
        generate_pass = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(size)])
        return generate_pass
    
    @classmethod
    def find_by_site_name(cls,site_name):
        for credential in cls.credential_list:
            if credential.site_name == site_name:
                return credential
    
    @classmethod
    def display_credentials(cls,user_name):
        user_credentials_list = []
        for credential in cls.credential_list:
            if credential.user_name == user_name:
                user_credentials_list.append(credential)
        return user_credentials_list
    
    @classmethod
    def copy_credentials(cls,site_name):
        found_credential = cls.find_by_site_name(site_name)
        return pyperclip.copy(found_credential.password)



      
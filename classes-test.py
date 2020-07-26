
import unittest
from classes import Users
from classes import Credentials
import pyperclip

class TestUsers(unittest.TestCase):
    def setUp(self):
        self.new_user = Users("Sam","Sam Smith","dhgkjjlk") 
        
    def test_init(self):
        self.assertEqual(self.new_user.user_name,"Sam")
        self.assertEqual(self.new_user.full_name,"Sam Smith")
        self.assertEqual(self.new_user.password,"dhgkjjlk")
    
    def test_save_user(self):
        self.new_user.save_user()
        self.assertEqual(len(Users.user_list),1)
    
    def tearDown(self):
        Users.user_list = []
    
    
    def test_delete_user(self):
        self.new_user.save_user()
        test_user = Users("Sam","Sam Smith","dhgkjjlk")
        test_user.save_user()
        self.new_user.delete_user()
        self.assertEqual(len(Users.user_list),1)
        



class TestCredential(unittest.TestCase):
    def setUp(self):
        self.new_credential = Credentials("Steve","Twitter","dfgfh")
    
    def test_init(self):
        self.assertEqual(self.new_credential.user_name,"Steve")
        self.assertEqual(self.new_credential.site_name,"Twitter")
        self.assertEqual(self.new_credential.password,"dfgfh")
    
    def tearDown(self):
        Credentials.credential_list = []
        Users.user_list = []
    
#     def test_save_credentials(self):
#         self.new_credential.save_credentials()
#         twitter = Credentials("Steve","Twitter","dfgfh")
#         twitter.save_credentials()
#         self.assertEqual(len(Credentials.credential_list),2)
    
#     def test_delete_credentials(self):
#         self.new_credential.save_credentials()
#         twitter = Credentials("Steve","Twitter","dfgfh")
#         twitter.save_credentials()
#         twitter.delete_credentials()
#         self.assertEqual(len(Credentials.credential_list),1)
    
#     def test_find_by_site_name(self):
#         self.new_credential.save_credentials()
#         twitter = Credentials("Steve","Twitter","dfgfh")
#         twitter.save_credentials()
#         credential_found = Credentials.find_by_site_name("Twitter")
#         self.assertEqual(credential_found.site_name,"Twitter")
    
#     def test_display_all_credentials(self):
#         self.assertEqual(Credentials.display_all_credentials(),Credentials.credential_list)
    
#     def test_copy_credentials(self):
#         self.new_credential.save_credentials()
#         twitter = Credentials("Steve","Twitter","dfgfh")
#         twitter.save_credentials = None
#         found_credential = None
#         for credential in Credentials.credential_list:
#             found_credential = Credentials.find_by_site_name(credential.site_name)
#             return pyperclip.copy(found_credential.password)
#         Credentials.copy_credentials(self.new_credential.site_name)
#         self.assertEqual("dfgfh",pyperclip.paste())
#         print(pyperclip.paste())


if __name__ == '__main__':
    unittest.main()

#!/usr/bin/env python3.6
import pyperclip
from classes import Users 
from classes import Credentials

 
def create_user(user_name,full_name,password):
    new_user = Users(user_name,full_name,password)
    return new_user

def create_credential(user_namez,site_name,passwordz):
    new_credential = Credentials(user_namez,site_name,passwordz)
    return new_credential

def save_user(user):
    return Users.save_user(user)

def display_users():
    return Users.display_users()

def save_credential(credential):
    return Credentials.save_credential(credential)

def authenticate_user(user_name,password):
    checking_user = Credentials.check_user(user_name,password)
    return checking_user

def rand_pass(size):
    return Credentials.rand_pass(size)

def display_credentials(user_name):
    return Credentials.display_credentials(user_name)

def delete_credential(credentials):
    Credentials.delete_credentials()

def copy_credentials(site_name):
    return Credentials.copy_credentials(site_name)

def find_by_site_name(site_name):
    return Credentials.find_by_site_name(site_name)

def main():
    print("Hello Welcome to your password locker.What is your name?")
    user_name = input()

    print(f"Hello {user_name}.What would you like to do it?")
    print('\n')

    while True:
        print("Use these short codes : ca-create a new account,ln- log in,ex-exit")

        short_code = input().lower()
        if short_code == "ex":
            print("Bye..")
            break

        elif short_code == 'ca':
            print("New User")
            print("-" * 10)

            print("Full Names:")
            full_name = input()

            print("Username:")
            user_name = input()

            print("Do you want to input your own password or have one generated for you? Use short codes\n'gp\' to generate password.\n \'cyo\' to choose your own password \n \'ex\' to exit...")
            password_choice = input()
            password = ''
            
            if password_choice == 'cyo':
                password = password.join(input("Enter your password"))
            
            elif password_choice == 'gp':
                print("Enter the length of the password you wish to generate for example 10")
                pass_len = int(input())
                password = rand_pass(pass_len)
            
            elif password_choice == 'ex':
                print("Bye")
                break
            else:
                print("Sorry I didn\'t get that. Please try again")
            
            
            save_user(create_user(user_name,full_name,password))
            print('/n')

            print(f"New account for {user_name} created.")
            print('/n')
            print(f"Password is {password} : Use to log in with shortcode ln")
            print('/n')
        
        elif short_code == 'ln':
            print('\n')
            print("Enter your account details to log in: \n Enter your fullnames...")
            user_name = input()
            print("Enter your password...")
            password = input()
            account_exist = authenticate_user(user_name, password)
            if account_exist == user_name:
                print('\n')
                print(f"Welcome to your Password locker account {user_name}: \n Please choose an option to continue...")
                print('\n')
                while True:
                    print('\n')
                    print("Navigation short codes: \n cc to create new credentials: \n dc to display credentials:  \n sc to search credentials: \n rm to remove or delete credentials: \n copy to copy credentials:  \n x to exit")
                    print('\n')
                    short_code = input().lower()
                    if short_code == 'cc':
                        print('\n')
                        print("Enter your credential details")
                        print("Enter account type... eg \'google\'")
                        site_name = input()
                        print(f"Enter username ")
                        user_namez = input()

                        while True:
                            print("Do you want to input your own password or have one generated for you? Use short codes\n'gp\' to generate password.\n \'cyo\' to choose your own password \n \'x\' to exit... ")
                            password_choice = input()
                            
                            
                            if password_choice == 'cyo':
                                passwordz = input(
                                    "Enter a password of your choice...")
                                break

                            elif password_choice == 'gp':
                                print(
                                    "Enter the length of the password you wish to generate eg 9 ")
                                pass_len = int(input())
                                passwordz = rand_pass(pass_len)
                                break

                            elif password_choice == 'x':
                                print('Goodbye.....')
                                break

                            else:

                                print("Sorry I didn\'t get that. Please try again")
                                break

                        save_credential(create_credential(user_namez,site_name,passwordz))
                        print(' - ' * 30)
                        print(f"Credential Created:\n Account type: {site_name}  \n Account Username: {user_namez} \n Account Password: {passwordz}")
                        print('-' * 30)

                    elif short_code == 'dc':
                        if display_credentials(user_namez):
                            print("Here is a list of your credentials:")
                            print('\n')
                            for credential in display_credentials(user_namez):
                                print(f"Credential Created:\n Account type: {site_name} \n Account Username: {user_namez} \n Account Password: {passwordz}")

                        else:
                            print("You don\'t have any credentials yet")
                    
                    elif short_code == 'sc':
                        print("Enter the account you want to search for")
                        site_name = input().lower()
                        if find_by_site_name(site_name):
                            search_credential = find_by_site_name(site_name)
                            print(f"Account Name: {search_credential.site_name}")
                            print(f"User Name: {search_credential.usernamez} Password : {search_credential.passwordz}")
                        else:
                            print("That credential does not exist")
                            print("\n")

                    elif short_code == 'rm':
                        print("Enter the account type of the credential you wish to delete:")
                        site_name = input()
                        if find_by_site_name(site_name):
                            credential_to__delete = find_by_site_name(site_name)
                            credential_to__delete.delete_credentials()
                            print("Credential successfuly deleted")
                        else:
                            print("That Credential does not exist")
                            print("\n")    

                    elif short_code == 'copy':
                        print("\n")
                        site_name = input("Enter the site name for the credential password to copy:")
                        if find_by_site_name(site_name):
                            credential_to_copy = find_by_site_name(site_name)
                            credential_to_copy.copy_credentials(site_name)

                            print("Credential successfully copied")
                    elif short_code == "x":
                         print('Goodbye.....')
                         break
                    else:
                        print("Invalid")
            else:
                print("I didn\'t get that, please try again")
                print('\n')

if __name__ == '__main__':
        main()


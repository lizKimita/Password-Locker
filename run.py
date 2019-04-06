#!/usr/bin/env python3.6

from user import User
from credentials import Credentials
import random
import string


#user functions
def create_new_user(first_name, last_name, user_name, password):
    '''
    Fuction to create new users
    '''
    new_user = User(first_name, last_name, user_name, password)
    return new_user

def save_user(user):
    '''
    Function to save a new uder account
    '''
    user.save_user

def verify_user(user_name):
    '''
    Function to check if a user exists from the user_list and returns a boolean
    '''
    return User.user_exists(user_name)
    
def delete_user(user):
    '''
    Fuction that allows users to delete their accounts
    '''
    user.delete_user()

#credentials Functions
def create_credentials(platform, account_user_name, account_password):
    '''
    Function that allows a user to create new credentials
    '''
    new_credentials = Credentials(platform, account_user_name, account_password)
    return new_credentials

def save_credentials(credentials):
    '''
    Function that allows users to save their credentials
    '''
    credentials.save_credentials()

def delete_credential(credentials):
    '''
    Function that allows a user to delete saved credentials
    '''
    credentials.delete_credentials()

def find_credentials(platform):
    '''
    Function that finds a credential using the platform
    '''
    return Credentials.find_by_platform(platform)


def check_existing_credentials(platform):
    '''
    Function to check if a user's credentials exist
    '''
    return Credentials.credentials_exist(platform)


def display_credentials():
    '''
    Function that returns all saved credentials
    '''
    return Credentials.display_saved_credentials()

def generate_password(self, size=8, char=string.ascii_uppercase+string.ascii_lowercase+string.digits):
    '''
    Function that gives a user the option to generate a new password automatically
    '''
    new_password = Credentials.generate_password(self, size=8, char=string.ascii_uppercase+string.ascii_lowercase+string.digits)
    return new_password

def main():
    print("Hello! Welcome to your personal password locker. What is your name?")
    user_name = input()

    print (f"Hello {user_name}. What would you like to do?")
    print('\n')

    while True:
        print(" Please Use these short codes to navigate: \n na - create a new Account, li - log into your account, da - delete your account, ex = exit the password locker app ")
            
        short_code = input().lower()

        if short_code == 'na':
            print("New Account")
            print("-"*10)   

            print("First Name.....")
            first_name = input()

            print("Last Name......") 
            last_name = input()

            print("User Name....")
            user_name = input()

            print("Password....")
            password = input()

            save_user (create_new_user(first_name, last_name, user_name, password))  
            print('\n')
            print(f"New Account for {first_name } {last_name } created")
            print (f'hello {first_name}, you are now logged in!')
            print('\n')
            while True:
                    print('To proceed use these shortcodes:\n cc - Create new Credentials, dc - Delete Credential, fd - Find Credential, ds - display saved credentials, ex - exit')
                    short_code = input().lower()
                    if short_code == 'ex':
                        print ('\n')
                        print(f'Goodbye { user_name}.')
                        break
                        
                    elif short_code == 'fd':
                        print ('\n')
                        print ('Enter the Platform you want to search for!')
                        search_platform = input()
                        if check_existing_credentials(search_platform):
                            search_credentials = find_credentials(search_platform)
                            print('\n')
                            print(f"Platform:{ search_credentials.platform}") 
                            print(f"User Name:{ search_credentials.account_user_name}") 
                            print(f"Account Password:{ search_credentials.account_password}")
                            print ('\n')
                        else:
                            print("That credential does not exist!")
                    elif short_code == 'ds':
                        if display_credentials():
                            print ('\n')
                            print('Here is a list of your saved credentials')
                            print('\n')

                            for credential in display_credentials():
                                print(f'Platform: { credential.platform}')
                                print('\n')
                                print(f'Account User Name: {credential.account_user_name}')
                                print(f'Account Password: {credential.account_password}')
                                print('\n')
                        else:
                            print ('\n')
                            print ('Looks like you haven\'t saved that credential yet!')
                            print ('\n')
                    elif short_code == 'cc':
                        print ('\n')
                        print ("New Credentials")
                        print ("-"*10)

                        print("Platform:")
                        platform = input()

                        print("Account user name:")
                        account_user_name = input()

                        print("Account Password:")
                        account_password = input()

                        save_credentials(create_credentials(platform, account_user_name, account_password))
                        print('\n')
                        print(f'New Credentials: {platform } {account_user_name } {account_password}')
                        print('\n')
     

        elif short_code =='ex':
            print("Have a lovely day!")
            break
        else:
            print('\n')
            print("I really didn't get that. Please use the short codes")
            print('\n')
if __name__ == '__main__':
     main()

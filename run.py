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

            print("Phone number....")
            user_name = input()

            print("Email address....")
            password = input()

            save_user (create_new_user(first_name, last_name, user_name, password))  
            print('\n')
            print(f"New User{first_name} {last_name} created")
            print('\n')

        elif short_code == 'dc':
            if display_contacts():
                print ("Here is a list of all your contacts")
                print('\n')

                for contact in display_contacts():
                    print(f"{contact.first_name}{contact.last_name}{contact.email}{contact.phone_number}")
                    print ('\n')
            else:
                    print('\n')
                    print("You don't seem to have any contacts yet")
                    print('\n')
            
        elif short_code == 'fc':
            print("Enter the number you want to search for")

            search_number = input()
            if check_existing_contacts(search_number):
                search_contact = find_contact(search_number)
                print(f"{search_contact.first_name} {search_contact.last_name}")
                print('-'*20)

                print(f"Phone number.......{search_contact.phone_number}")
                print(f"Email address......{search_contact.email}")
            else:
                print("That contact does not exist")

        elif short_code =='ex':
            print("Bye......")
            break

        else:
            print("I really didn't get that. Please use the short codes")

if __name__ == '__main__':
     main()

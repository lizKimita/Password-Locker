#!/usr/bin/env python3.6

from user import User
from credentials import Credentials

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

def generate_password():
    '''
    Function that allows users to generate their passwords
    '''

def delete_user():
    '''
    Fuction that allows users to delete their accounts
    '''

#credentials Functions
import random
import string
import pyperclip


class Credentials:
    '''
    Class to generate new instances of the user's credentials.
    ''' 
    credentials_list = []

    def __init__(self, platform, account_user_name, account_password):  
        '''
        init__helps us to define our credentials properties.

        Args:
            platform: New user's platform
            account_user_name: New user_name for the platform
            account_password:New password for the platform
        '''

        self.platform = platform
        self.account_user_name = account_user_name
        self.account_password = account_password

    def save_credentials(self):
        '''
        save_credentials method saves credentials objects into the credentials_list
        '''
        Credentials.credentials_list.append(self)

    def delete_credentials(self):
        '''
        delete_credentials method deletes a user's credentials from the credentials_list
        '''
        Credentials.credentials_list.remove(self)

    def generate_password(self, size=8, char=string.ascii_uppercase+string.ascii_lowercase+string.digits):
        '''
        generate_password method that generates an 8 character password
        '''
        gen_pass=''.join(random.choice(char) for _ in range(size))
        return gen_pass

    @classmethod
    def find_by_account_user_name(cls,account_user_name):
        '''
        Method that takes in a user's user_name and displays his or her saved credentials

        Args:
            account_user_name:User_name to search for
        Returns: 
            The Credentials saved by that user
        '''

        for credentials in cls.credentials_list:
            if credentials.account_user_name == account_user_name:
                return credentials

    @classmethod
    def credentials_exist(cls, account_user_name):
        '''
        Method that checks if a credential exists fron the credentials_list

        Args:
            account_user_name:user_ name to search if it exists
        Returns:
            Boolean: True or false depending on if it exists
        '''
        for credentials in cls.credentials_list:
            if credentials.account_user_name ==account_user_name:
                return True

        return False
    
    @classmethod
    def display_saved_credentials(cls):
        '''
        method to display a user's saved credentials
        '''
        return cls.credentials_list




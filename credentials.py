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
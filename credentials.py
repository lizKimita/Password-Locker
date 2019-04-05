class Credentials:
    '''
    Class to generate new instances of the user's credentials.
    ''' 

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
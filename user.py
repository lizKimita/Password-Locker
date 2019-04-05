class User:
    '''
    Class that generates new instances of the user.
    '''
    
    def __init__(self, first_name, last_name, user_name, password):
        '''
        init__helps us to define our users' properties.

        Args:
            first_name: New contact first name.
            last_name: New contact last name.
            user_name: New user's login username.
            password: New user's login password   
        '''

        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.password = password


    
class User:
    '''
    Class that generates new instances of the user.
    '''
    user_list = []

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

    def save_user(self):
        '''
        Method saves user objects into the user_list
        '''
        User.user_list.append(self)

    def delete_user(self):
        '''
        Delete_user method deletes a saved user from the user_list 
        '''
        User.user_list.remove(self)

    @classmethod
    def find_by_user_name(cls, user_name):
        '''
        Method that takes in a user_name and returns the user details that match that user_name

        Args:
            user_name: User_ name to search for
        Returns: 
            User Details of the person that matches that user_name.
        '''

        for user in cls.user_list:
            if user.user_name == user_name:
                return user
    
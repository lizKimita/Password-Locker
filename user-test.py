import unittest
from user import User

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user and credentials class behaviours.

    Args: 
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Setup method to run before each test case
        '''
        self.new_user = User("Liz", "Kimita", "Shiko", "shikolove")

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.first_name,"Liz")
        self.assertEqual(self.new_user.last_name,"Kimita")
        self.assertEqual(self.new_user.user_name, "Shiko")
        self.assertEqual(self.new_user.password, "shikolove")

    def test_save_user(self):
        '''
        test_save_user test case to test if a new user is saved into the user_list
        '''
        self.new_user.save_user()
        self. assertEqual(len(User.user_list),1)

    def test_save_multiple_users(self):
        '''
        test_save_multiple_users test case to test if multiple users can be saved into our user_list
        '''
        self.new_user.save_user()
        test_user = User ("Kevin", "Kittony", "Kevkip", "kipkenya")
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)

if __name__ == '__main__':
    unittest.main()
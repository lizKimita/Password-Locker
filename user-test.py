import unittest
from user import User
import pyperclip

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

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.user_list = []

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

    def test_delete_user(self):
        '''
        test_delete_user test case to test if we can remove a user from our user's list
        '''
        self.new_user.save_user()
        test_user = User("Njoki", "kimita", "jnnjoki", "njokikim")
        test_user.save_user()

        self.new_user.delete_user()
        self.assertEqual(len(User.user_list),1)

    def test_find_user_by_user_name(self):
        '''
        Test to check if we can find a user by their username and display their details"
        '''
        self.new_user.save_user()
        test_user = User("Ngesh", "Mwathi", "angesh", "ngeshy")
        test_user.save_user()

        find_user = User.find_by_user_name("angesh")

        self.assertEqual(find_user.password, test_user.password)

    def test_user_exists(self):
        '''
        Test to check if we can return a boolean if we cannot find a user
        '''

        self.new_user.save_user()
        test_user = User("Grace", "Muigai", "gMuigai", "qwerty")
        test_user.save_user()

        user_exists = User.user_exists("gMuigai")

        self.assertTrue(user_exists)

    def test_password_generator(self):
        '''
        Test to check if user can generate random passwords should they choose to generate passwords
        '''



if __name__ == '__main__':
    unittest.main()
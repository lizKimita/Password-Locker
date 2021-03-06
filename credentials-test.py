import pyperclip
import unittest
from credentials import Credentials

class TestCredentials(unittest.TestCase):
    '''
    Test  class that defines test cases for the credentials class behaviours.

     Args: 
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Setup method to run before each test case
        '''
        self.new_credentials = Credentials("Twitter", "lizkimita", "twitshiko")

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_credentials.platform,"Twitter")
        self.assertEqual(self.new_credentials.account_user_name,"lizkimita")
        self.assertEqual(self.new_credentials.account_password, "twitshiko")

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Credentials.credentials_list = []

    def test_save_credentials(self):
        '''
        test_save_credentials to check if the user credentials are being saved in the credentials_list
        '''
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)

    def test_save_multiple_credentials(self):
        '''
        test_save_multiple_credentials to check if we can save multiple credentials into our credentials_list
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials("Facebook", "fbgeek", "faceconnect")
        test_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),2)

    def test_delete_credentials(self):
        '''
        test_delete_credentials to test if a user can remove a credential from the credentials_list
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials("Instagram","kareflo", "karekim")
        test_credentials.save_credentials()

        self.new_credentials.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)

    def test_find_credentials_by_platform(self):
        '''
        Test to check if we can find a user's credentials the platform and display the details
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials("Glassdoor", "wilmwangi", "jobwil")
        test_credentials.save_credentials()

        find_credentials = Credentials.find_by_platform("Glassdoor")

        self.assertEqual(find_credentials.account_user_name, test_credentials.account_user_name)

    def test_credentials_exist(self):
        '''
        test to check if we can return a boolean if we cannot find the searched for credentials
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials("LinkedIn", "kimk", "shikolinkd")
        test_credentials.save_credentials()

        credentials_exist = Credentials.credentials_exist("LinkedIn")

        self.assertTrue(credentials_exist)

    def test_display_saved_credentials(self):
        '''
        method that displays all the saved credentials
        '''
        self.assertEqual(Credentials.display_saved_credentials(),Credentials.credentials_list)
        

if __name__ == '__main__':
    unittest.main()
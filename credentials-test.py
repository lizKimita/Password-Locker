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

if __name__ == '__main__':
    unittest.main()